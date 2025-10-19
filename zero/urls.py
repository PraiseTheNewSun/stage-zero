from django.contrib import admin
from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('me', ProfileView.as_view({'get': 'list'}), name='profile-view'),
]