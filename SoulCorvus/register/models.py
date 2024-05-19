from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Customer(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="Customer")
    user_permissions = models.ManyToManyField(Permission, related_name="user_permissions_set")