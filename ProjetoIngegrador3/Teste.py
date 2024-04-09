from myapp.models import User
# Create a new instance of the User model
user_instance = User(username='John', password='examplepassword', access_level=2)

# Save the instance to the database
user_instance.save()