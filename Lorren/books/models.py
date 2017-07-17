from django.db import models

from authors.models import Author

class Book(models.Model):
    title =  models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, blank=False)
    year = models.IntegerField(blank=False)
    rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, blank=False)
    comment = models.TextField(max_length=300)
    rating = models.IntegerField(default=0, blank=False)
