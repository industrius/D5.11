from django.urls import path
from . import views

urlpatterns = [
    path("", views.BooksView.as_view()),
    path("book/<int:id>/", views.BookDetails.as_view()),
    path("author/<int:id>/", views.AuthorDetails.as_view()),
    path("increment", views.book_increment),
    path("decrement", views.book_decrement),
    path("authors", views.AuthorsView.as_view()),
    path("publishers", views.PublishersView.as_view()),
    path("publisher/<int:id>", views.PublisherDetail.as_view()),
    path("friends", views.FriendsView.as_view()),
    path("friend/<int:id>", views.FriendDetails.as_view()),
    path("give_to_friend", views.give_to_friend),
    path("return_book", views.return_book),
    path("book/new", views.CreateBook),
    path("author/new/<int:toggle>", views.CreateAuthor),
    path("publisher/new/<int:toggle>", views.CreatePublisher),
    path("friend/new", views.CreateFriend),
    path("author/delete", views.DeleteAuthor),
    path("publisher/delete", views.DeletePublisher),
    path("friend/delete", views.DeleteFriend),
    path("book/delete", views.DeleteBook)
]