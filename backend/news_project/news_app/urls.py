from django.urls import path, include
from news_app.views import PostViewSet, TagViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='users')

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet, basename='posts')

tag_router = DefaultRouter()
tag_router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
   path('', include(user_router.urls)),
   path('', include(post_router.urls)), 
   path('', include(tag_router.urls)),
]