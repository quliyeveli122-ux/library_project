from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pages = models.PositiveBigIntegerField()
    is_available = models.BooleanField(default=True)
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
