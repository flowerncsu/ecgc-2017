from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    # Automagically has username, password, email, first_name, and last_name fields
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)