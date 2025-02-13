from django.contrib import admin
from .models import PantryItem, FridgeItem, FreezerItem

admin.site.register(PantryItem)
admin.site.register(FridgeItem)
admin.site.register(FreezerItem)