from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['first_name', 'last_name']]
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    FICTION = 'fiction'
    TEXTBOOK = 'textbook'
    CATEGORY_CHOICES = [
        (FICTION, 'Художественное произведение'),
        (TEXTBOOK, 'Учебник'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=FICTION)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['title', 'author', 'publication_year', 'publisher']]
        ordering = ['title', 'publication_year']

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


