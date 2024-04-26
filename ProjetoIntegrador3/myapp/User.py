from django.core.management.base import BaseCommand
from django.shortcuts import render
from django.conf import settings
from .models import User
import psycopg2
from psycopg2 import Error

# Define the connection string
POSTGRES_URL = "postgres://default:ZgvNJnU6W7BR@ep-aged-thunder-a458v4ko-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

def get_users_access_levels():
    users_access_levels = {}
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(POSTGRES_URL)

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Fetch user access levels from the database
        cursor.execute("SELECT username, level FROM User_Table")
        user_table_records = cursor.fetchall()
        for record in user_table_records:
            users_access_levels[record[0]] = record[1]

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)

    return users_access_levels

def my_view(request):
    # Get users' access levels either from Django model or from the database
    users_access_levels = get_users_access_levels()

    # Utilize access levels
    required_levels = {"admin": 1, "editor": 2, "viewer": 3}  # Define access levels based on user roles

    # Check access levels for each user
    for username, level in users_access_levels.items():
        if username in required_levels:
            if level <= required_levels[username]:
                print(f"{username} has access to perform this action.")
            else:
                print(f"{username} does not have sufficient access level.")
        else:
            print(f"No access level defined for user: {username}")

    return render(request, 'my_template.html')