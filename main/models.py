from django.db import models

class Features(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    img_logo = models.ImageField(upload_to='images/', default='default.jpg')
    url = models.URLField(default='bodyMeasure.html')

class About(models.Model):
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='images/', default='default.jpg')

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    

        
        