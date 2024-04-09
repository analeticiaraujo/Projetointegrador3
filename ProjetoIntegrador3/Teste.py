import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'ProjetoIntegrador3.settings'  # Replace 'ProjetoIntegrador3.settings' with your actual settings module
POSTGRES_URL = "postgres://default:ZgvNJnU6W7BR@ep-aged-thunder-a458v4ko-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

# Manually setup Django's application registry
django.setup()

# Now you can import your Django models
from myapp.models import User

# Import other necessary modules
import unittest
import psycopg2
from django.test import TestCase

class TestCreateUser(TestCase):
    @classmethod
    def setUpClass(cls):
        # Establish a connection to the database
        cls.connection = psycopg2.connect(POSTGRES_URL)
        cls.cursor = cls.connection.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the cursor and connection
        cls.cursor.close()
        cls.connection.close()

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
            print("Error creating user:", e)
            # Fail the test explicitly with the exception message
            self.fail("Error creating user: " + str(e))

        # Check if the user exists in the database
        self.cursor.execute("SELECT * FROM myapp_user WHERE username = 'test_user'")
        user_record = self.cursor.fetchone()
        self.assertIsNotNone(user_record)
    
    # Clean up after the test
        new_user.delete()

if __name__ == '__main__':
    unittest.main()