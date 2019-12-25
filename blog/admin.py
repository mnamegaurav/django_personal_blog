from django.contrib import admin

# Register your models here.
from .models import Article, ContactMeData, Comment

#registration for Article model
admin.site.register(Article)

#registration for ContactMeData model
admin.site.register(ContactMeData)

#registration for Comment model
admin.site.register(Comment)