from django.db import models

from authors.models import Author

class Book(models.Model):
    title =  models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, blank=False)
    year = models.IntegerField(blank=False)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def update_rating(self):
        comments = Comment.objects.all().filter(book=self)
        total = 0
        average = 0
        if comments:
            for comment in comments:
                total += comment.rating

            average = round(total / len(comments),1)
        self.rating = average
        self.save()

class Comment(models.Model):
    book = models.ForeignKey(Book, blank=False)
    message = models.TextField(max_length=300)
    rating = models.IntegerField(default=0, blank=False)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        self.book.update_rating()
