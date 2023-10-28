import random
import string
from django.contrib.auth.models import User
from django.db import models
from account.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

def generate_unique_code():
    code_length = 6
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    friends = models.ManyToManyField(CustomUser, related_name='user_friends')

    def __str__(self):
        return self.user.username

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(UserProfile)
    unique_code = models.CharField(max_length=6,blank=True, unique=True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Group)
def generate_group_unique_code(sender, instance, **kwargs):
    if not instance.unique_code:
        instance.unique_code = generate_unique_code()