from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# class Category(models.Model):

#     NAMES = [
#     ('Cat1','Educational'),
#     ('Cat2','Technology'),
#     ('Cat3','Tutorial'),
#     ('Cat4','News')]

#     name = models.CharField(max_length=20,null=True,choices=NAMES,default=NAMES[0][0])

#     def __str__(self):
#         return self.name

class Article(models.Model):

    title = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    date_published = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=100)

    body = models.TextField()

    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    CHOICES = [
    ('EDUCATIONAL','Educational'),
    ('TECHNOLOGY','Technology'),
    ('TUTORIAL','Tutorial'),
    ('NEWS','News')]

    category = models.CharField(max_length=20, choices=CHOICES,null=True)

    likes = models.ManyToManyField(User, related_name='likes',blank=True)

    dislikes = models.ManyToManyField(User, related_name='dislikes',blank=True)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    # def total_likes(self):
    #     return self.

    # def total_dislikes(self):
    #     return self.dislikes.count()

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug':self.slug})


class ContactMeData(models.Model):

    email = models.EmailField()

    full_name = models.CharField(max_length=30)

    city = models.CharField(max_length=15)

    zip_code = models.IntegerField()

    say_something = models.CharField(max_length=200)

    def __str__(self):
        return self.email
