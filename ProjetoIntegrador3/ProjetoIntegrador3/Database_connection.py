import psycopg2

# Connection parameters
dbname = 'verceldb'
user = 'default'
password = 'ZgvNJnU6W7BR'
host = 'ep-aged-thunder-a458v4ko-pooler.us-east-1.aws.neon.tech'
port = '5432'

# Establishing a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Creating a cursor object using the connection
    cursor = connection.cursor()

    # Executing a sample query
    cursor.execute('SELECT version()')

    # Fetching the result
    db_version = cursor.fetchone()
    print("Connected to:", db_version)

    # Closing the cursor and the connection
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)