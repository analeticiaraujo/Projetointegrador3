from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=50)
    stored_password = models.CharField(max_length=50)
    level = models.IntegerField()
    

    def has_access(self, required_level):
        return self.level >= required_level
    
class Client(models.Model):
    registration_id = models.CharField(max_length=100)
    client_type = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)

class Bills(models.Model):
    #ADD CLIENT FOREIGN KEY and VALUE IF THE BILL IS OF THE PROCESS
    payment_id = models.CharField(max_length=100)
    day_of_payment = models.DateField()
    type_of_bill = models.CharField(max_length=100)
    fiscal_note = models.CharField(max_length=100)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=100)

class Payment(models.Model):
    process = models.CharField(max_length=100)
    received_value = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)