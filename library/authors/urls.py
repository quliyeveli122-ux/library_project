from django.urls import path

from .views import (
    AuthorCreateAPIView, 
    AuthorListAPIView,
    AuthorDetailAPIView,
    AuthorDeleteAPIView,
    AuthorUpdateAPIView
)


urlpatterns = [
    path(
        "authors/create/",
        AuthorCreateAPIView.as_view(),
        name="author-create"
    ),
    path(
        "authors/",
        AuthorListAPIView.as_view(),
        name="authors"
    ),
    path(
        "authors/<int:author_id>/",
        AuthorDetailAPIView.as_view(),
        name="author-detail"
    ),
    path(
        "authors/<int:author_id>/delete/",
        AuthorDeleteAPIView.as_view(),
        name="author-delete"
    ),
    path(
        "authors/<int:author_id>/update/",
        AuthorUpdateAPIView.as_view(),
        name="author-update"
    )
]
