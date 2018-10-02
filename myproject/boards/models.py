from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    last_updated = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')