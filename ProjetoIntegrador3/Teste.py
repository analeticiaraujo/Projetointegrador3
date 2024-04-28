import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'ProjetoIntegrador3.settings'  # Replace 'ProjetoIntegrador3.settings' with your actual settings module

# Manually setup Django's application registry
django.setup()

# Now you can import your Django models
from myapp.models import User

# Import other necessary modules
from django.test import TestCase

class TestCreateUser(TestCase):
    def test_create_user(self):
        try:
            # Attempt to create a new user
            new_user = User.objects.create(username='test_user', stored_password='teste', level=1)
            
            # Fetch the user record from the database
            user_record = User.objects.get(username='test_user')
            
            # Check if the user record is not None
            self.assertIsNotNone(user_record)
        except Exception as e:
            # If an exception occurs during user creation, print the exception
            self.fail("Error creating user: " + str(e))

    # Ensure that changes made during the test are rolled back after the test completes
    def tearDown(self):
        try:
            # Delete the test user if it exists
            User.objects.filter(username='test_user').delete()
        except Exception as e:
            # If an exception occurs during cleanup, print the exception
            self.fail("Error cleaning up: " + str(e))

if __name__ == '__main__':
    import unittest
    unittest.main()