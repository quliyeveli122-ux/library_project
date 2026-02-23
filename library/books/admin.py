from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'is_available', 'published_date')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('is_available', 'published_date', 'author')
    list_editable = ('price', 'is_available')
