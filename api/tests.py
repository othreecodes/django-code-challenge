import json
from django.test import TestCase
from rest_framework_jwt.serializers import (
    jwt_encode_handler,
    jwt_payload_handler,
)
from rest_framework.test import APITestCase
from api import factories
from api.models import ContactList


class WhenCreatingOrUpdatingAList(APITestCase):
    def setUp(self):
        user = factories.UserFactory()
        payload = jwt_payload_handler(user)
        self.token = jwt_encode_handler(payload)

    def test_authenticated_user_can_create_a_new_contact(self):
        payload = {"name": "Mr Samuel", "email": "sam@gmail.com"}
        auth = f"JWT {self.token}"
        response = self.client.post(
            "/list/new",
            data=json.dumps(payload),
            HTTP_AUTHORIZATION=auth,
            content_type="application/json",
        )
        result = response.json()
        self.assertEqual(response.status_code, 201)
        contact = ContactList.objects.get(pk=result["id"])
        self.assertEqual(payload["name"], contact.name)
        self.assertEqual(payload["email"], contact.email)

    def test_unauthenticated_user_cannot_create_a_new_contact(self):
        payload = {"name": "Mr Samuel", "email": "sam@gmail.com"}
        # auth = f"JWT {self.token}"
        response = self.client.post(
            "/list/new",
            data=json.dumps(payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_fetch_a_list_of_contacts(self):
        factories.ContactListFactory.create_batch(5)
        auth = f"JWT {self.token}"
        response = self.client.get(
            f"/list", HTTP_AUTHORIZATION=auth, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        result = response.json()

        self.assertEqual(len(result), 5)
        self.assertEqual(ContactList.objects.count(), 5)
        for contact in result:
            self.assertIsNotNone(contact["name"])
            self.assertIsNotNone(contact["email"])

    def test_authenticated_user_can_fetch_a_single_contact(self):
        instance = factories.ContactListFactory()
        auth = f"JWT {self.token}"
        response = self.client.get(
            f"/list/{instance.pk}",
            HTTP_AUTHORIZATION=auth,
            content_type="application/json",
        )

        result = response.json()
        self.assertEqual(response.status_code, 200)

        self.assertEqual(instance.name, result["name"])
        self.assertEqual(instance.id, result["id"])
        self.assertEqual(instance.email, result["email"])

    def test_authenticated_user_can_update_a_single_contact(self):
        instance = factories.ContactListFactory(
            name="Ayo", email="oldemail@email.com"
        )

        self.assertEqual(instance.email, "oldemail@email.com")
        auth = f"JWT {self.token}"
        payload = {"name": "Ayo", "email": "newemail@gmail.com"}
        response = self.client.put(
            f"/list/{instance.pk}",
            HTTP_AUTHORIZATION=auth,
            data=json.dumps(payload),
            content_type="application/json",
        )

        result = response.json()

        self.assertEqual(response.status_code, 200)

        contact = ContactList.objects.get(pk=result["id"])

        self.assertEqual(contact.email, "newemail@gmail.com")
        self.assertEqual(contact.name, "Ayo")

    def test_authenticated_user_can_delete_a_single_contact(self):
        instance = factories.ContactListFactory()
        auth = f"JWT {self.token}"
        response = self.client.delete(
            f"/list/{instance.pk}",
            HTTP_AUTHORIZATION=auth,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 204)
        self.assertFalse(ContactList.objects.filter(id=instance.id).exists())
