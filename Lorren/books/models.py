from django.db import models

from authors.models import Author

class Book(models.Model):
    title =  models.CharField(max_length=100)
    author = models.ForeignKey(Author, default=None, blank=False)
    year = models.IntegerField(blank=False)

    def __str__(self):
        return self.title
