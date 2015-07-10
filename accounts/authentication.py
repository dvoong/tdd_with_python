from django.contrib.auth import get_user_model
from django.conf import settings
import requests

User = get_user_model()

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'

class PersonaAuthenticationBackend(object):
    
    def authenticate(self, assertion):
        response = requests.post(PERSONA_VERIFY_URL, data={'audience': settings.DOMAIN, 'assertion': assertion})
        if response.ok == False:
            return None

        if response.json()['status'] != 'okay':
            return None
        try:
            user = User.objects.get(email=response.json()['email'])
            return user
        except User.DoesNotExist:
            user = User.objects.create(email=response.json()['email'])
            return user

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
