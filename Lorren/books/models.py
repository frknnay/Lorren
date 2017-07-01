from django.db import models

from authors.models import Author

class Book(models.Model):
    title =  models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, blank=False)
    year = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, blank=False)
    rate = models.IntegerField(blank=False)
    message = models.TextField()
