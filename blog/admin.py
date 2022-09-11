from django.contrib import admin
from blog.models import Category, Comment, Like, Post, PostView

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Comment)