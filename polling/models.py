from django.db import models

from identity.models import User


class Polling(models.Model):
    data_structure = models.CharField(max_length=1, blank=True, null=True)
    algorithm = models.CharField(max_length=1, blank=True, null=True)
    cplusplus = models.CharField(max_length=1, blank=True, null=True, verbose_name='C++')
    python = models.CharField(max_length=1, blank=True, null=True)
    java = models.CharField(max_length=1, blank=True, null=True)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polling")
    ip = models.CharField(max_length=155, blank=True, null=True)
