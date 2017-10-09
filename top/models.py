from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    vue =  models.IntegerField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.title