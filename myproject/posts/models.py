from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)

    def __reper__(self):
        return self.title
