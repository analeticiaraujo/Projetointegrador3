import psycopg2
from psycopg2 import Error

# Define the connection string
POSTGRES_URL = "postgres://default:ZgvNJnU6W7BR@ep-aged-thunder-a458v4ko-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

try:
    # Establish a connection to the database
    connection = psycopg2.connect(POSTGRES_URL)

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Fetch all records from the bill_payments table
    cursor.execute("SELECT * FROM bill_payments")
    bill_payments_records = cursor.fetchall()
    print("Bill Payments:")
    for record in bill_payments_records:
        print(record)

    # Fetch all records from the entry_values table
    cursor.execute("SELECT * FROM entry_values")
    entry_values_records = cursor.fetchall()
    print("\nEntry Values:")
    for record in entry_values_records:
        print(record)

    # Fetch all records from the User_Table table
    cursor.execute("SELECT * FROM User_Table")
    user_table_records = cursor.fetchall()
    print("\nUser Table:")
    for record in user_table_records:
        print(record)

    # Fetch all records from the client_registration table
    cursor.execute("SELECT * FROM client_registration")
    client_registration_records = cursor.fetchall()
    print("\nClient Registration:")
    for record in client_registration_records:
        print(record)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)