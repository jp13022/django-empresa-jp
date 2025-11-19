from django.urls import path
from .views import cupons

urlpatterns = [
    path('cupons/', cupons, name="cupons"),
]
