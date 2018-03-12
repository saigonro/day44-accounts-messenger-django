
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', inbox, name='inbox'),
    url(r'sent/', sent, name='sent'),
    url(r'view_message/(\d+)$', view_message, name='view_message'),
    url(r'compose_message/', compose_message, name='compose_message'),
]