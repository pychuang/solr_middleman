from django.db import models

# Create your models here.
class Query(models.Model):
    q = models.CharField(max_length=1000)
