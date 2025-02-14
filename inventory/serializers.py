from rest_framework import serializers
from .models import PantryItem, FridgeItem, FreezerItem

# Serializer for PantryItem model
class PantryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryItem
        exclude = ('user',)

# Serializer for FridgeItem model
class FridgeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FridgeItem
        exclude = ('user',)

# Serializer for FreezerItem model
class FreezerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreezerItem
        exclude = ('user',)
        