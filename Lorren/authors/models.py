from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=240, blank=False)

    def __str__(self):
        return self.name
