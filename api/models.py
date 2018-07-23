from django.db import models


class ContactList(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "{}-{}".format(self.name, self.email)
