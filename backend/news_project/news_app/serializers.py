from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from news_app.models import Post, Tag, User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model        = Tag
        fields       = '__all__'

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model        = Post
        fields       = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):    
    posts = PostSerializer(many=True, required=False)
    class Meta:
        model        = User
        fields       = ('username', 'email', 'profile_image', 'posts')
        extra_kwargs = {
            'password':{
                'write_only':'True',
                'style': {'input_type': 'password'}
            }
        } 
    def validate_password(self, value: str) -> str:
        return make_password(value)