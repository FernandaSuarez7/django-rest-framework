from django.db import models

# Create your models here.


class Programmer(models.Model):
    Nombre = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)