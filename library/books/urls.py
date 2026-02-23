from django.urls import path

from .views import (
    BookCreateAPIView, 
    BookListAPIView,
    BookDetailAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView
)


urlpatterns = [
    path(
        "books/create/",
        BookCreateAPIView.as_view(),
        name="book-create"
    ),
    path(
        "books/",
        BookListAPIView.as_view(),
        name="books"
    ),
    path(
        "books/<int:book_id>/",
        BookDetailAPIView.as_view(),
        name="book-detail"
    ),
    path(
        "books/<int:book_id>/delete/",
        BookDeleteAPIView.as_view(),
        name="book-delete"
    ),
    path(
        "books/<int:book_id>/update/",
        BookUpdateAPIView.as_view(),
        name="book-update"
    )
]
