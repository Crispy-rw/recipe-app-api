from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successfull"""
        email = "test@localhost.com"
        password = "12345678"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_normalized(self):
        """
            Test the email for a new User is normalized
        """
        email = 'test@LOCALHOST.COM'
        user = get_user_model().objects.create_user(
            email,
            'test@123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ 
            Test Creating a user with no Email raises Error
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_new_superuser(self):
        """
            Creating a new SuperUser
        """

        user = get_user_model().objects.create_superuser(
            'test@localhpst.com',
            '12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
