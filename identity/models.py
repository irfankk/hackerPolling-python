from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True)
    challenges_solved = models.CharField(max_length=255, blank=True, verbose_name='No of challenges solved')

    @property
    def full_name(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        elif self.email:
            return self.email
        else:
            return self.username

    def __str__(self):
        return self.full_name