from rest_framework import serializers
from users.models import User


class UserSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    
    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data ["first_name"]
        instance.last_name = validated_data ["last_name"]
        instance.username = validated_data ["username"]
        instance.email = validated_data ["email"]
        instance.password = validated_data ["password"]

        instance.save()
        return instance
    
    def update(self,instance, validated_data):
        instance.first_name = validated_data ["first_name"]
        instance.last_name = validated_data ["last_name"]
        instance.username = validated_data ["username"]
        instance.email = validated_data ["email"]
        instance.password = validated_data ["password"]

        instance.save()
        return instance
    

        