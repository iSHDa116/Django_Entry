from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=15)
    publication_date = models.DateField()
    def __str__(self):
        return self.title