from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


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
    media_file = models.FileField(upload_to='private_music/', null=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class PublicMusicRecord(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    media_file = models.FileField(upload_to='public_music/', null=True)

    def __str__(self):
        return self.name


class ProtectedMusicRecord(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    email_ids = ArrayField(models.CharField(max_length=100), default=list)
    media_file = models.FileField(upload_to='protected_music/', null=True)

    def __str__(self):
        return self.name
