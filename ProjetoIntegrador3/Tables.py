import psycopg2
from psycopg2 import Error

# Define the connection string
POSTGRES_URL = "postgres://default:ZgvNJnU6W7BR@ep-aged-thunder-a458v4ko-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

try:
    # Establish a connection to the database
    connection = psycopg2.connect(POSTGRES_URL)

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Fetch all records from the User_Table table
    cursor.execute("SELECT * FROM User_Table")

    # Fetch column names from the description attribute of cursor
    column_names = [desc[0] for desc in cursor.description]
    print("\nColumn Names in User_Table:")
    print(column_names)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)