from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import ContactList


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactList
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        write_only_fields = ("password",)
        fields = ("first_name", "last_name", "username", "email", "password")
