from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
import django.utils
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to='images/profile/', default="/static/theblog/images/default_profile_pic.jpg")
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    @property
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/theblog/images/default_profile_pic.jpg"

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default="xxx")
    snippet = models.CharField(
        max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=255)

    def __str__(self):
        return '% s - %s' % (self.post.title, self.name)


"""
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
"""
