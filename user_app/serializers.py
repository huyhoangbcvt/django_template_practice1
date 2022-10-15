from rest_framework import serializers
from .models.account_model import Profile


class User_appSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
