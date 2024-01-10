from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.comment[:10]}"
