from django.db import models

class Skill_text(models.Model):
    title = models.CharField(max_length=15)
    text1 = models.CharField(max_length=60)
    text2 = models.CharField(max_length=150)
    def __str__(self):
        return "skill_text"

class Skill(models.Model):
    name = models.CharField(max_length=20)
    persent = models.IntegerField()
    right = models.BooleanField()
    def __str__(self):
        return self.name
