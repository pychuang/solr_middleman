from django.db import models

# Create your models here.
class Query(models.Model):
    q = models.TextField()
