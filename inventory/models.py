from django.db import models
from django.contrib.auth.models import User

# Abstract base class to avoid repeating common fields across inventory items
class BaseInventoryItem(models.Model):
    # Links item to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    expiration_date = models.DateField(null=True, blank=True)
    # Automatically stores when the item was added
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # prevents django from creating a separate table for this class
        abstract = True

# Specific models inheriting from BaseInventoryItem
class PantryItem(BaseInventoryItem):
    pass

class FridgeItem(BaseInventoryItem):
    pass

class FreezerItem(BaseInventoryItem):
    pass
