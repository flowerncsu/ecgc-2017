from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)


class InventoryListing(models.Model):
    item = models.ForeignKey(Item)
