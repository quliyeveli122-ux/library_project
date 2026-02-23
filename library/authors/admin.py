from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country', 'birth_date', 'created_at')
    search_fields = ('first_name', 'last_name', 'country')
    list_filter = ('country', 'created_at')
    list_display_links = ('id', 'first_name', 'last_name')
