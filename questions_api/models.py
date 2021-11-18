from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)

class Comment(models.Model):
    comment=models.CharField(max_length=(120))
    question=models.ManyToManyField(Question)

class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    comment=models.ManyToManyField(Comment)
    question = models.ManyToManyField(Question)