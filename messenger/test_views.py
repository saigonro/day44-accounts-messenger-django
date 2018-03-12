from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class MessageViewsTest(TestCase):
    def test_inbox_template(self):
        response = self.client.get('/messenger/')
        self.assertTemplateUsed(response, 'messenger/inbox.html')
    def test_sent_template(self):
        response = self.client.get('/messenger/sent/')
        self.assertTemplateUsed(response, 'messenger/sent.html')
    def test_compose_message_template(self):
        response = self.client.get('/messenger/compose_message/')
        self.assertTemplateUsed(response, 'messenger/compose_message.html')
    def test_view_message_404_template(self):
        response = self.client.get('/messenger/view_message/1')
        self.assertEqual(response.status_code, 404)
        
    def test_view_message_that_exists(self):
        sender = User(username="sender")
        sender.save()

        recipient = User(username="receiver")
        recipient.save()

        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()

        response = self.client.get('/messenger/view_message/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messenger/view_message.html")
        
    def test_post_message(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')
        self.client.login(username="sender", password="sender")
        
        message = {
            "subject": "Test Subject",
            "body": "Test Body",
            "recipient": recipient.id
        }

        response = self.client.post('/messenger/compose_message/', message)
        self.assertEqual(response.status_code, 302)
        
    # def test_viewing_a_message_marks_it_as_read(self):
    #     sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
    #     recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')

    #     message = Message(
    #         subject = "Test Subject",
    #         body = "Test Body",
    #         sender = sender,
    #         recipient = recipient)
    #     message.save()

    #     self.assertEqual(message.read, False)
        
    #     response = self.client.get('/messenger/message/1')
        
    #     message = get_object_or_404(Message, pk=1)
    #     self.assertEqual(message.read, True)