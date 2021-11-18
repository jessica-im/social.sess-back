from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)

class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
