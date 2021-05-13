from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=20000)
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images/")
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title