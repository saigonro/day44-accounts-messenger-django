from django.test import TestCase
from .views import *
from django.core.urlresolvers import resolve

# Create your tests here.

class MessengerPageTest(TestCase):
    def test_messenger_inbox_test_home_page_resolves(self):
        messenger_home_page = resolve('/messenger/')
        self.assertEqual(messenger_home_page.func, inbox)
    def test_messenger_sent_test_home_page_resolves(self):
        messenger_sent_home_page = resolve('/messenger/sent/')
        self.assertEqual(messenger_sent_home_page.func, sent)
    def test_messenger_view_message_test_home_page_resolves(self):
        messenger_view_message_home_page = resolve('/messenger/view_message/1')
        self.assertEqual(messenger_view_message_home_page.func, view_message)
    def test_messenger_compose_message_test_home_page_resolves(self):
        messenger_compose_message_home_page = resolve('/messenger/compose_message/')
        self.assertEqual(messenger_compose_message_home_page.func, compose_message)
        
    def test_message_require_id(self):
        response = self.client.get('/messenger/message/')
        self.assertEqual(response.status_code, 404)
