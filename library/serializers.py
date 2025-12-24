from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Author
        fields = [
            'id',
            'first_name',
            'last_name',
            'full_name',
            'biography',
            'birth_date',
            'death_date',
            'books_count',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_books_count(self, obj):
        return obj.books.count()


class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True)
    cover_image_url = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'author_name',
            'publication_year',
            'genre',
            'category',
            'category_display',
            'publisher',
            'cover_image',
            'cover_image_url',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return None


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    cover_image_url = serializers.SerializerMethodField()
    book_file_url = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'author_id',
            'publication_year',
            'genre',
            'category',
            'category_display',
            'publisher',
            'cover_image',
            'cover_image_url',
            'book_file',
            'book_file_url',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return None

    def get_book_file_url(self, obj):
        if obj.book_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.book_file.url)
            return obj.book_file.url
        return None



