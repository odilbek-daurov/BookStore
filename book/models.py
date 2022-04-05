from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='author/')

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='book/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # status = models.BooleanField()
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
