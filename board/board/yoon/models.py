from django.db import models
class User(models.Model):
    name = models.CharField(max_length=20)
class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
