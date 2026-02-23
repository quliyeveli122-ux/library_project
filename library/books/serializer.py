from rest_framework.serializers import ModelSerializer

from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "published_date",
            "price",
            "pages",
            "is_available",
            "author",
            "created_at"
        ]
