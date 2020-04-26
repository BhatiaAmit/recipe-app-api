from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        email = "amit@india.com"
        password = "Test@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        email = "amit@INDIA.COM"
        user = get_user_model().objects.create_user(email, "Test@123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test133")

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser("amit1@india.com", "test133")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
