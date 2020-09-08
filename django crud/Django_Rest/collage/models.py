from django.db import models

# Create your models here.

class Collage(models.Model):
    name = models.CharField(max_length=222,unique=True)
    image = models.ImageField(upload_to='media/post_image',blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
