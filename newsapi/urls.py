from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Directly use the root URL for home page
]
