from django.db import models
from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=14)
    href = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Home(models.Model):
    line1 = models.CharField(max_length=15)
    line2 = models.CharField(max_length=20)
    line3 = models.CharField(max_length=30)
    line4 = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    job =models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    facebook = models.URLField()
    twitter = models.URLField()
    github = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return "home_page_model"