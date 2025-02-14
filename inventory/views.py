from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PantryItem, FridgeItem, FreezerItem
from .serializers import PantryItemSerializer, FridgeItemSerializer, FreezerItemSerializer

# API View for Pantry items
class PantryItemListCreateView(generics.ListCreateAPIView):
    # converts model data to JSON
    serializer_class = PantryItemSerializer
    # ensures only logged-in users can access 
    permission_classes = [IsAuthenticated]

    # fetch user's pantry items only
    def get_queryset(self):
        return PantryItem.objects.filter(user=self.request.user)
    
    # assigns the item to the logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PantryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PantryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PantryItem.objects.filter(user=self.request.user)
    
# API View for Fridge items
class FridgeItemListCreateView(generics.ListCreateAPIView):
    serializer_class = FridgeItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FridgeItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FridgeItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FridgeItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FridgeItem.objects.filter(user=self.request.user)

# API View for Freezer items
class FreezerItemListCreateView(generics.ListCreateAPIView):
    serializer_class = FreezerItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FreezerItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FreezerItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FreezerItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FreezerItem.objects.filter(user=self.request.user)
    

