from django.test import TestCase
from .models import SignUp
# Create your tests here.

class SignUpTestCase(TestCase):
    def setUp(self):
        SignUp.objects.create(full_name="Gaurav testing")
    def test_signup_name(self):
        obj=SignUp.objects.get(id=4)
        self.assertEqual(obj.full_name,'A new title')