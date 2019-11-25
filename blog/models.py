from django.db import models
import datetime
from django.contrib.auth.models import User



class Article(models.Model):

    title = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    date_published = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=100)

    body = models.TextField()

    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ContactMeData(models.Model):

    email = models.EmailField()

    full_name = models.CharField(max_length=30)

    city = models.CharField(max_length=15)

    zip_code = models.IntegerField()

    say_something = models.CharField(max_length=200)

    def __str__(self):
        return self.email
