from django.urls import path
from .views import api, booksAPI, oneBookAPI

urlpatterns = [
    path("hello/", api),
    path("books/", booksAPI),
    path("onebook/<int:bookid>", oneBookAPI),
]