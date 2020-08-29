from django import template
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Book, Author, Publisher, Friend
from .forms import AuthorForm, BookForm, FriendForm, PublisherForm

class BooksView(View):
    """
    Вывод списка книг
    """
    def get(self, request):
        books = Book.objects.all().order_by("title")
        return render(request, "books.html", {"books_list": books, "books_active": "active"})

class BookDetails(View):
    """
    Информация о выбранной книге
    Друзья, которые эту книгу арендуют
    """
    def get(self, request, id):
        book = Book.objects.get(id=id)
        friends = book.friends.all()
        all_friends = Friend.objects.all()
        return render(request, "book_details.html", {"book": book,"friends_list": friends, "all_friends_list": all_friends, "books_active": "active"})

class AuthorsView(View):
    """
    Вывод списка авторов с количеством 
    книг, которые они написали
    """
    def get(self, request):
        authors = Author.objects.all().order_by("full_name")
        for author in authors:
            author.books_count = Book.objects.filter(author=author).count()
        return render(request, "authors.html", {"authors_list": authors, "authors_active": "active"})

class AuthorDetails(View):
    """
    Информация об выбранном авторе и количестве его книг в коллекции
    """
    def get(self, request, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)
        return render(request, "author_details.html", {"author": author, "books_list": books, "authors_active": "active"})

class PublishersView(View):
    """
    Вывод списка издателей и количества их книг в библиотеке
    """
    def get(self, request):
        publishers = Publisher.objects.all().order_by("title")
        for publisher in publishers:
            publisher.books_count = Book.objects.filter(publisher=publisher).count()
        return render(request, "publishers.html", {"publishers_list": publishers, "publishers_active": "active"})

class PublisherDetail(View):
    """
    Информация о выбранном издателе и 
    список их книг в библиотеке
    """
    def get(self, request, id):
        publisher = Publisher.objects.get(id=id)
        books = Book.objects.filter(publisher=publisher)
        return render(request, "publisher_details.html", {"publisher": publisher, "books_list": books, "publishers_active": "active"})

class FriendsView(View):
    """
    Вывод списка друзей и количества книг, которые они арендовали
    """
    def get(self, request):
        friends = Friend.objects.all().order_by("full_name")
        return render(request, "friends.html", {"friends_list": friends, "friends_active":"active"})

class FriendDetails(View):
    """
    Информация о выбранном друге и книгах, которые он арендовал
    А так же кнопка для возврата книги в библиотеку
    """
    def get(self, request, id):
        friend = Friend.objects.get(id=id)
        books = Book.objects.all()
        return render(request, "friend_details.html", {"friend":friend, "books_list": books,"friends_active":"active"})

class ShowError(View):
    """
    Показывает страницу ошибки
    """
    def get(self, request):
        return render(request, "error.html")

def book_increment(request):
    """
    Обработка увеличения количества экземпляров книги в библиотеке
    Кнопки увеличения и уменьшения на странице книги
    """
    if request.method == "POST":
        id = request.POST["id"]
        book = Book.objects.filter(id = id).first()
        book.copy_count += 1
        book.save()
        return redirect("book/" + id)
    else:
        return redirect("/")

def book_decrement(request):
    """
    Обработка уменьшения количества экземпляров книги в библиотеке
    Кнопки увеличения и уменьшения на странице книги
    """
    if request.method == "POST":
        id = request.POST["id"]
        book = Book.objects.filter(id = id).first()
        if book.copy_count > 0:
            book.copy_count -= 1
            book.save()
        return redirect("book/" + id)
    else:
        return redirect("/")

def give_to_friend(request):
    """
    Обработка передачи экземпляра книги в аренду выбранному другу
    Функционал на странице книги
    """
    if request.method == "POST":
        book_id = request.POST["book_id"]
        friend_id = request.POST["friend_id"]
        if friend_id != "":
            book = Book.objects.filter(id=book_id).first()
            friend = Friend.objects.filter(id=friend_id).first()
            if book.copy_count > 0:
                if not friend in book.friends.all():
                    book.copy_count -= 1
                    book.friends.add(friend)
                    book.save()
        return redirect("book/" + book_id)

def return_book(request):
    """
    Обработка возврата экземпляра книги в библиотеку
    Функционал со страницы друга
    """
    if request.method == "POST":
        book_id = request.POST["book_id"]
        friend_id = request.POST["friend_id"]
        book = Book.objects.filter(id=book_id).first()
        friend = Friend.objects.filter(id=friend_id).first()
        book.copy_count += 1
        book.friends.remove(friend)
        book.save()
        return redirect("friend/" + friend_id)

def CreateBook(request):
    """
    Обработка добавления новой книги в библиотеку
    Функционал на странице списка книг
    """
    book_form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/error")
    else:
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        return render(request, "create_book.html", {"book_form": book_form, "authors_list": authors, "publishers_list": publishers, "books_active": "active"})

def CreateAuthor(request, toggle):
    """
    Обработка добавления нового автора 
    Функционал на странице списка авторов
    """
    author_form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            if toggle == 0:
                return redirect("/authors")
            else:
                return redirect("/book/new")
        else:
            return redirect("/error")
    else:
        return render(request, "create_author.html", {"author_form": author_form, "toggle":toggle, "authors_active": "active"})

def CreatePublisher(request, toggle):
    """
    Обработка добавления нового издателя 
    Функционал на странице списка издателей
    """
    publisher_form = PublisherForm()
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            if toggle == 0:
                return redirect("/publishers")
            else:
                return redirect("/book/new")
        else:
            return redirect("/error")
    else:
        return render(request, "create_publisher.html", {"publisher_form": publisher_form, "toggle":toggle, "publishers_active": "active"})

def CreateFriend(request):
    """
    Обработка добавления нового друга 
    Функционал на странице списка друзей
    """
    friend_form = FriendForm()
    if request.method == "POST":
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/friends")
        else:
            return redirect("/error")
    else:
        return render(request, "create_friend.html", {"friend_form": friend_form, "friends_active":"active"})

def DeleteAuthor(request):
    """
    Обработка удаления автора 
    Функционал на странице списка авторов
    """
    if request.method == "POST":
        author = Author.objects.filter(id=request.POST["author_id"])
        author.delete()
    return redirect("/authors")

def DeletePublisher(request):
    """
    Обработка удаления издателя 
    Функционал на странице списка издателей
    """
    if request.method == "POST":
        publisher = Publisher.objects.filter(id=request.POST["publisher_id"])
        publisher.delete()
    return redirect("/publishers")

def DeleteFriend(request):
    """
    Обработка удаления друга 
    Функционал на странице списка друзей
    """
    if request.method == "POST":
        friend = Friend.objects.filter(id=request.POST["friend_id"]).first()
        books = Book.objects.filter(friends=friend)
        for book in books:
            book.copy_count += 1
            book.friends.remove(friend)
            book.save()
        friend.delete()
    return redirect("/friends")

def DeleteBook(request):
    """
    Обработка удаления книги 
    Функционал на странице книги
    """
    if request.method == "POST":
        book = Book.objects.filter(id=request.POST["book_id"]).first()
        book.delete()
    return redirect("/")