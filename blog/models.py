from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to ='album/photo')
    description = models.TextField()
    short_description = models.TextField()
    creation = models.DateTimeField(auto_now_add= True)
