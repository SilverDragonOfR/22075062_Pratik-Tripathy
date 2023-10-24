from django.db import models

# Create your models here.
class URL(models.Model):
    short_url = models.CharField(max_length=8, unique=True)
    long_url = models.CharField(max_length=10000)