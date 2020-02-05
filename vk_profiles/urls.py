from django.urls import path, include
from .models import Profile
from .views import ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'api/profile', ProfileViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
