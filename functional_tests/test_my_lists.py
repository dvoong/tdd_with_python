from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session

class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)
        ## to set a cookie we need to first visit the domain
        ## 404 pages load the quickest
        print('test_my_lists.py: session_key: {}'.format(session_key))
        self.browser.get(self.server_url + "/404_no_such_url")
        self.browser.add_cookie(dict(
                name=settings.SESSION_COOKIE_NAME,
                value=session_key,
                path='/',
                ))
    
    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        
        self.browser.get(self.server_url)
        self.wait_to_be_logged_out(email)

        # Edith is a logged in user
        self.create_pre_authenticated_session(email)

        self.browser.get(self.server_url)
        from django.conf import settings
        from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
        User = get_user_model()
        from django.contrib.sessions.backends.db import SessionStore
#         print('create_session.py: backend_session: {}'.format(session))
#         print('SESSION_KEY:', SESSION_KEY)
#         print('session[SESSION_KEY]:', session[SESSION_KEY])
#         print('BACKEND_SESSION_KEY:', BACKEND_SESSION_KEY)
#         print('session[BACKEND_SESSION_KEY]:', session[BACKEND_SESSION_KEY])
#         print('session.keys():', session.keys())
#         print('session.session_key:', session.session_key)
#         print('type(session.session_key)', type(session.session_key))

        print('test_my_lists.py: cookies: {}'.format(self.browser.get_cookies()))
        self.wait_to_be_logged_in(email)

        
