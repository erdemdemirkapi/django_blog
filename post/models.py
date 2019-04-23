from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    publishing_date = models.DateTimeField()

    def __str__(self):
        return self.title