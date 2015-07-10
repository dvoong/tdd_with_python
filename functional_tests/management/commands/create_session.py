from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('email')

    def handle(self, email, *_, **__):
        session_key = create_pre_authenticated_session(email)
        self.stdout.write(session_key)

def create_pre_authenticated_session(email):
    user = User.objects.create(email=email)
    session = SessionStore()
    session[SESSION_KEY] = user.pk
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session.save()
    print('create_session.py: backend_session: {}'.format(session))
    print('SESSION_KEY:', SESSION_KEY)
    print('session[SESSION_KEY]:', session[SESSION_KEY])
    print('BACKEND_SESSION_KEY:', BACKEND_SESSION_KEY)
    print('session[BACKEND_SESSION_KEY]:', session[BACKEND_SESSION_KEY])
    print('session.keys():', session.keys())
    print('session.session_key:', session.session_key)
    print('type(session.session_key)', type(session.session_key))
    return session.session_key

