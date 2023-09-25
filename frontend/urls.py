
from django.urls import path
# Include frontend.urls
from django.urls import include
from .views import index

urlpatterns = [
    path('', index),
]
