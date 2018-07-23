from rest_framework import serializers
from api.models import ContactList


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactList
        fields = "__all__"
