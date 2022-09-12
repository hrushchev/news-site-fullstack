from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from news_app.models import User

class UserProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model        = User
        fields       = ('id' ,'email' ,'username' ,'password')
        extra_kwargs = {
            'password':{
                'write_only':'True',
                'style': {'input_type': 'password'}
            }
        } 
    def validate_password(self, value: str) -> str:
        return make_password(value)