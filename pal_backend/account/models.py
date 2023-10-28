import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)  # Add the UUID field
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
