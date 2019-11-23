from django.contrib import admin

# Register your models here.
from .models import Article, ContactMeData

#registration for Article model
admin.site.register(Article)

#registration for ContactMeData model
admin.site.register(ContactMeData)
