from rest_framework.serializers import ModelSerializer

from .models import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "country",
            "created_at"
        ]
