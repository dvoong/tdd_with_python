from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'
    last_login = models.DateTimeField(default=timezone.now)

    def is_authenticated(self):
        return True
