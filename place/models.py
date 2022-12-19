from django.db import models
# Create your models here.

from django.contrib.auth import get_user_model

class Place(models.Model):
    name = models.CharField(max_length=256)
    Administrator=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    descrpition=models.TextField(blank=True)

    def __str__(self):
        return self.name