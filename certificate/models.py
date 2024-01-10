from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='certificates')
    description = models.TextField()
    def __str__(self):
        return self.name


class Certificate_text(models.Model):
    title = models.CharField(max_length=50)
    text1 = models.TextField()
    text2 = models.TextField()
    category1 = models.CharField(max_length=30) # all
    category2 = models.CharField(max_length=30) # web
    category3 = models.CharField(max_length=30) # develpment
    category4 = models.CharField(max_length=30) # mobile
    def __str__(self):
        return self.title