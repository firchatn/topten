from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    vue =  models.IntegerField()
    date = models.CharField(max_length=20)
    lien = models.CharField(max_length=200)
    img = models.ImageField(upload_to='upload/',blank=True)

    def __str__(self):
        return self.title