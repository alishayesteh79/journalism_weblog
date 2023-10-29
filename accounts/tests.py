from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignUpTests(TestCase):
    def test_url_view_templates(self):
        response1 = self.client.get('/accounts/signup/')
        self.assertEqual(response1.status_code, 200)
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
'registration/signup.html')

    def test_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'testuser',
                'age' : '21',
                'email' : 'test@test.com',
                'password1' : '123456Aa@',
                'password2' : '123456Aa@'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().
count(), 1)
        self.assertEqual(get_user_model().objects.all()
[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()
[0].email , 'test@test.com')
        self.assertEqual(get_user_model().objects.all()
[0].age, 21)