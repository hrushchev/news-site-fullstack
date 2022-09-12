from rest_framework import viewsets

from news_app.models import User
from news_app.serializers import UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

class PostViewSet(viewsets.ViewSet):
    pass
