from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    header_title = models.CharField(max_length=255)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='img/author_images/')
    square_profile_pic = models.ImageField(null=True, blank=True, upload_to='img/square_author_images/')
    location = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='img/blog_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
