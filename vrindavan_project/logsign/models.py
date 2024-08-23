from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)  # Added full_name field
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.full_name  # Display full name in string representation

