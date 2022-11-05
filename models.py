from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ObjpythctDoesNotExist

class profile(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    firstname = models.CharField(max_length=255, primary_key=True)
    lastname = models.CharField(max_length=255, primary_key=True)
    email = models.CharField(max_length=255, primary_key=True)
    event = models.CharField(null=True, blank=True)
    proficiencyLevel = models.CharField(null=True, blank=True)
    searchingForMembers = models.IntegerField(null=True, blank=True)
    frameworks = models.JSONField(null=True, blank=True)
    languages = models.JSONField(null=True, blank=True)
    stacks = models.JSONField(null=True, blank=True)
    suggestions = models.JSONField(null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def __str__(self):
        return self.id


class framework(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.id

class language(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.id

class stack(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.id



