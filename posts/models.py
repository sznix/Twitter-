from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta:
        db_table = 'post'
        ordering = ['-created_at']

    name = models.CharField(max_length=14, default='Anonymous')
    body = models.TextField(max_length=140, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    likecount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.body[:50]}'
