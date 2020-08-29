from django.contrib import admin
from .models import Author, Book, Friend, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Friend)
admin.site.register(Publisher)