import factory.fuzzy
from django.contrib.auth.models import User


class ContactListFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "First_user-{0}".format(n))
    email = factory.Sequence(lambda n: "user-{0}@example.com".format(n))

    class Meta:
        model = "api.ContactList"


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: "First_user-{0}".format(n))
    last_name = factory.Sequence(lambda n: "Last_user-{0}".format(n))
    email = factory.Sequence(lambda n: "user-{0}@example.com".format(n))
    password = factory.PostGenerationMethodCall("set_password", "password")
    username = factory.Sequence(lambda n: "user-{0}".format(n))

    class Meta:
        model = User
        django_get_or_create = ("username",)
