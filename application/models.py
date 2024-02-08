from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.IntegerField()
    state=models.CharField(max_length=20)
