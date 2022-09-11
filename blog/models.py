from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"

class Post(models.Model):
    STATUS = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to="")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    published_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Post"