from django.db import models
from django.utils import timezone

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogapp/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title