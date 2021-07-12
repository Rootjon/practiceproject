from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to='slider_images/')
    short_description = models.TextField()


    def __str__(self):
        return self.headline


class Feature(models.Model):
    haedline = models.CharField(max_length=100)
    thumbnail =models.ImageField(upload_to ='carousel/images/')
    slug = models.SlugField()
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.haedline
