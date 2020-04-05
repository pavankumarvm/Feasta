from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FeastaUser, MessOwner, Consumer

UserModel = get_user_model()

class FeastaUserSerializer(serializers.ModelSerializer):
    """
        Serailize the FeastaUser data
    """
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email', 'phone_no', 'first_name', 'last_name', 'date_joined', 'last_login' ,'is_messowner', 'is_consumer']
        read_only_fields = ('date_joined', 'last_login')

    def create(self, validated_data):
        return FeastaUser.objects.create(**validated_data)

class MessOwnerSerializer(serializers.ModelSerializer):
    """
        Serialize the Messowner data
    """
    class Meta:
        model = MessOwner
        fields = "__all__"

    def create(self, validated_data):
        return MessOwner.objects.create(**validated_data)

class ConsumerSerializer(serializers.ModelSerializer):

    """
        Serialize the Consumer data
    """
    class Meta:
        model = Consumer
        fields = "__all__"