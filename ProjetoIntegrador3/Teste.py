import os
import unittest
import psycopg2
from django.test import TestCase
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'ProjetoIntegrador3.settings'  # Replace 'your_project.settings' with your actual settings module
POSTGRES_URL = "postgres://default:ZgvNJnU6W7BR@ep-aged-thunder-a458v4ko-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

# Manually setup Django's application registry
import django
django.setup()

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
        # Delay import of models until Django's app registry is ready
        from myapp.models import User  # Adjust this import based on your actual app structure

        # Assuming you have a User model in your Django app
        new_user = User.objects.create(username='test_user', access_level=1)
        self.assertIsNotNone(new_user)

        # Check if the user exists in the database
        self.cursor.execute("SELECT * FROM User_Table WHERE username = 'test_user'")
        user_record = self.cursor.fetchone()
        self.assertIsNotNone(user_record)
        # Clean up after the test
        new_user.delete()

if __name__ == '__main__':
    unittest.main()