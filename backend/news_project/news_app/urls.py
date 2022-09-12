from django.urls import path, include
from news_app.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
   path('', include(router.urls)),
]