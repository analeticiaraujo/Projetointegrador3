# Generated by Django 5.0.3 on 2024-04-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_clientregistration_remove_invoice_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]