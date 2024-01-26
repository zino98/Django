from django.urls import path
from .views import api
from .views import booksAPI

urlpatterns = [
    path("hello/", api),
    path("books/", booksAPI),
]