from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'death_date', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'biography')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'category', 'publisher', 'created_at')
    list_filter = ('category', 'genre', 'publication_year', 'created_at')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'genre', 'publisher')
    readonly_fields = ('created_at', 'updated_at')


