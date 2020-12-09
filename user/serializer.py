from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ["date_joined", "is_active"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exist")
        return value

    def validate_phone_number(self, value):
        if len(value) != 8:
            raise serializers.ValidationError("Phone number is not valid")
        return value

    def create(self, validated_data):
        user = User(email=validated_data["email"], first_name=validated_data["first_name"], last_name=validated_data["last_name"], phone_number=validated_data["phone_number"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    

