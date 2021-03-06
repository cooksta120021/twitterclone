from django.contrib.auth.models import AbstractUser
from django.db import models


class NewUser(AbstractUser):
    following = models.ManyToManyField('self',symmetrical=False)