from django import forms
from .models import Author, Book, Publisher, Friend

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = "__all__"