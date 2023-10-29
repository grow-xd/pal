# commondates/models.py
from django.db import models

class CommonDate(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"Common date in {self.location}: {self.date}"
