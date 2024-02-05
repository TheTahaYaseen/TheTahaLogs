from django.db import models

# Create your models here.
class Log(models.Model):
    subject = models.CharField(max_length=255)
    log = models.TextField()
    visibility = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)