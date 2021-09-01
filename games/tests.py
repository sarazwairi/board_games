from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class game_crud_test(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='admin',
            email='sara.zwairi@gmail.com',
            password='sama'
        )
    def test_create_user(self):
        self.assertEquals(self.user.email,'sara.zwairi@gmail.com')
        self.assertEquals(self.user.username,'admin')

    