from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.serializers import ContactListSerializer, UserSerializer
from api.models import ContactList
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User

class ContactListViewSet(ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer

    @list_route(methods=["POST"])
    def new(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer