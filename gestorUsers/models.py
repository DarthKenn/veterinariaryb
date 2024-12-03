from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    es_administrador = models.BooleanField(default=False)
    es_usuario_normal = models.BooleanField(default=True)

    def __str__(self):
        return self.username
