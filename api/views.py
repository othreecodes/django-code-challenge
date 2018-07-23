from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route
from api.serializers import ContactListSerializer
from api.models import ContactList


class ContactListViewSet(ModelViewSet):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer

    @list_route(methods=["POST"])
    def new(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
