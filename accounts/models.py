from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    # Automagically has username, password, email, first name, and last name fields
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    inventory = models.ManyToManyField('items.InventoryListing', reverse_name='owner')