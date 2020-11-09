from rest_framework import serializers
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'img', 'phone', 'email']
    
    def create(self, validated_data):
        if validated_data:
            user = User.objects.create_user(
                username=validated_data['username'],
                img=validated_data.get('img', None),
                phone=validated_data.get('phone', None),
                email=validated_data['email']
            )

            user.set_password(validated_data['password'])
            user.save()
            return user



class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'img', 'phone', 'email']