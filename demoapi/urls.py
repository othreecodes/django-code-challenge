"""demoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import ContactListViewSet, UserViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter(trailing_slash=False)

router.register(r"list", ContactListViewSet, "list")
router.register(r"user", UserViewSet, "user")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", obtain_jwt_token, name="login"),
]

urlpatterns.extend(router.urls)
