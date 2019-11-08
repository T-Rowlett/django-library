from django.db import models
from datetime import datetime
# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    published = models.TimeField(datetime.now)
    genre = models.TextField()
    in_stock = models.BooleanField()
    description = models.TextField()

class Transaction(models.Model):
    datetime = models.TimeField(datetime.now)
    action = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)



