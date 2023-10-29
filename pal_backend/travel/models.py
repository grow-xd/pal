from django.db import models
from account.models import CustomUser 

class Travel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    available_dates = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s travel to {self.location}"
