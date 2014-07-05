from pyquery import PyQuery
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from captcha.models import CaptchaStore
from contacts.models import Message


# Create your tests here.
class MessagePostTest(TestCase):
    def get_captcha_hash(self):
        html = self.client.get(reverse("contacts:show_form"))
        p = PyQuery(html.content)
        return p('#id_captcha_0').attr('value')

    def test_message_validation(self):
        # bad email and no captcha -> server-side validation
        msg = {"name": "ina", "email": "bad email",
               "phone": 123, "text": "a test message"}
        response = self.client.post(reverse("contacts:show_form"), msg)
        p = PyQuery(response.content)
        self.assertEqual(len(p('.form-group.has-error')), 2)
        self.assertContains(response, "Enter a valid email address.")
        self.assertContains(response, "This field is required.")
        # now bad captcha only
        msg = {"name": "ina", "email": "ok@email.ru",
               "phone": 123, "text": "a test message",
               "captcha_0": self.get_captcha_hash(),
               "captcha_1": "BAD GUESS"}
        response = self.client.post(reverse("contacts:show_form"), msg)
        p = PyQuery(response.content)
        self.assertEqual(len(p('.form-group.has-error')), 1)
        self.assertContains(response, "Invalid CAPTCHA")
        # TODO should write tests for client side validation as well

    def test_send_message(self):
        captcha0 = self.get_captcha_hash()
        captcha1 = CaptchaStore.objects.filter(hashkey=captcha0)
        self.assertEqual(len(captcha1), 1)
        captcha1 = captcha1[0].challenge
        msg = {"name": "ina", "email": "ina@test.ru",
               "phone": 123, "text": "a test message",
               "captcha_0": captcha0,
               "captcha_1": captcha1}
        sent_text = \
            "Спасибо! Мы получили Ваше сообщение и в скором времени свяжемся с Вами! =)"
        # test that after post message is shown in database
        db_msg = Message.objects.filter(sender_email=msg["email"])
        self.assertTrue(len(db_msg) == 0)
        response = self.client.post(reverse("contacts:show_form"), msg,
                                    follow=True)
        self.assertTrue(response.status_code == 200)
        # verify that message-sent page is shown
        last_redir_url = response.redirect_chain[-1][0]
        self.assertTrue(reverse("contacts:message_sent") in last_redir_url)
        self.assertContains(response, sent_text)
        # test that after post message is shown in database
        db_msg = Message.objects.filter(sender_email=msg["email"])
        self.assertTrue(len(db_msg) == 1)

    def test_no_message_edit_in_admin(self):

        def get_admin_url(msg):
            return reverse("admin:%s_%s_change" %
                           (msg._meta.app_label, msg._meta.module_name), args=(msg.id,))

        User.objects.create_superuser('admin', 'admin@test.ru', 'password')
        msg = Message(sender_email="ina@test.ru", sender_name="ina",
                      text="bla-bla-bla", phone="123", pub_date=timezone.now())
        msg.save()
        # now login and see that message can't be modified
        r = self.client.login(username='admin', password='password')
        self.assertTrue(r)
        edit_html = self.client.get(get_admin_url(msg)).content
        p = PyQuery(edit_html)
        # make sure there are no buttons at all (save\save and create another)
        self.assertTrue(len(p("input[type='submit']")) == 0)
