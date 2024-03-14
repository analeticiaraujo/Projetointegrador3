class User:
    def __init__(self, username, password, access_level):
        self.username = username
        self.password = password
        self.access_level = access_level

    def has_access(self, required_level):
        return self.access_level >= required_level


user1 = User("admin", "admin123", 3)  # Full access
user2 = User("editor", "editor123", 2)  # Limited access
user3 = User("viewer", "viewer123", 1)  # View only access

# Checking access levels
print(user1.has_access(3))  # True
print(user2.has_access(3))  # False
print(user3.has_access(3))  # False
print(user2.has_access(2))  # True
print(user3.has_access(2))  # False
print(user3.has_access(1))  # True
