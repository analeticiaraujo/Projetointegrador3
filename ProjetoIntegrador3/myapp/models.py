from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    level = models.IntegerField()
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def has_access(self, required_level):
        return self.level >= required_level
    def __str__(self):
        return self.username
    
@receiver(pre_save, sender=User)
def check_duplicate_username(sender, instance, **kwargs):
    # Check if there's another user with the same username
    existing_user = User.objects.filter(username=instance.username).exclude(id=instance.id).first()
    if existing_user:
        # Delete the existing user with the same username
        existing_user.delete()

    
    
class ClientRegistration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=100)
    client_type = models.CharField(max_length=20)
    identifier = models.CharField(max_length=14)
    legal_action = models.CharField(default='', max_length=100),
    def __str__(self):
        return self.client

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
