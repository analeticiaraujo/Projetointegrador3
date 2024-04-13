from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=50)
    stored_password = models.CharField(max_length=50)
    level = models.IntegerField()
    

    def has_access(self, required_level):
        return self.level >= required_level
    
class ClientRegistration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=100)
    client_type = models.CharField(max_length=20)
    identifier = models.CharField(max_length=14)

class EntryValue(models.Model):
    legal_action = models.CharField(max_length=100)
    received_value = models.DecimalField(max_digits=15, decimal_places=2)
    client = models.ForeignKey(ClientRegistration, on_delete=models.CASCADE)

class BillPayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    day_of_payment = models.DateField()
    type_of_bill = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    registration = models.ForeignKey(ClientRegistration, on_delete=models.CASCADE)
