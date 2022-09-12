from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from news_app.models import Post, Tag, User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model        = Tag
        fields       = ('id', 'title')

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model        = Post
        fields       = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        tags_to_apply = []

        for tag_data in tags_data:
            Tag.objects.get_or_create(**tag_data)
            current_tag = Tag.objects.filter(title=tag_data['title']).values_list('id', flat=True)
            print(current_tag)
            tags_to_apply += current_tag

        for tag in tags_to_apply:
            post.tags.add(tag)

        return post

class UserProfileSerializer(serializers.ModelSerializer):    
    posts = PostSerializer(many=True, required=False)
    class Meta:
        model        = User
        fields       = ('id', 'username', 'email', 'profile_image', 'posts')
        extra_kwargs = {
            'password':{
                'write_only':'True',
                'style': {'input_type': 'password'}
            }
        } 
    def validate_password(self, value: str) -> str:
        return make_password(value)