from django.db import models

class AboutMe(models.Model):
    line1 = models.CharField(max_length=15)
    line2 = models.CharField(max_length=60)
    line3 = models.CharField(max_length=20)
    line4 = models.CharField(max_length=20)
    line5 = models.CharField(max_length=20)
    btn = models.CharField(max_length=15)
    image = models.ImageField(upload_to='aboutme')

    def __str__(self):
        return 'about me object'


class Info(models.Model):
    feild = models.CharField(max_length=60)
    def __str__(self):
        return self.feild
