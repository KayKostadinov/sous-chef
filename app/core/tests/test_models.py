from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        '''Test creating a new user with email succeeds'''
        email = 'kay@kay.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email, password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test normalized email'''
        email = 'kay@Kay.com'
        user = get_user_model().objects.create_user(email, 'testpassword')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testtest')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'kay@kay.com',
            'testpassword'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
