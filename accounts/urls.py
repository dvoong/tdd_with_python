from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login$', 'accounts.views.persona_login', name='persona_login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
]
