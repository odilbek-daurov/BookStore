from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book
# Create your models here.


class MyUser(AbstractUser):
    image = models.ImageField(upload_to='user/',null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_order')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_order')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.book
