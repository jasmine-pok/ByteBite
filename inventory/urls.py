from django.urls import path
from .views import (
    PantryItemListCreateView, PantryItemDetailView,
    FridgeItemListCreateView, FridgeItemDetailView,
    FreezerItemListCreateView, FreezerItemDetailView
)

urlpatterns = [
    # Pantry Endpoints
    path('pantry/', PantryItemListCreateView.as_view(), name='pantry-list-create'),
    path('pantry/<int:pk>/', PantryItemDetailView.as_view(), name='pantry-detail'),

    # Fridge Endpoints
    path('fridge/', FridgeItemListCreateView.as_view(), name='fridge-list-create'),
    path('fridge/<int:pk>/', FridgeItemDetailView.as_view(), name='fridge-detail'),

    # Freezer Endpoints
    path('freezer/', FreezerItemListCreateView.as_view(), name='freezer-list-create'),
    path('freezer/<int:pk>/', FreezerItemDetailView.as_view(), name='freezer-detail'),
]