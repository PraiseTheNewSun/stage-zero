from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter #type: ignore
from zero.views import ProfileView

router = DefaultRouter()
router.register('me', ProfileView, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zero.urls')),
    path('', include(router.urls))
]
