from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NewUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.CharField(max_length=5, unique=True)
    email_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PrivateMusicRecord(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class PublicMusicRecord(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class ProtectedMusicRecord(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    email_id = ArrayField(models.CharField(max_length=10), default=list)

    def __str__(self):
        return self.name
