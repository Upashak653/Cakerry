# Generated by Django 5.1.1 on 2024-09-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0006_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Username',
            field=models.CharField(max_length=40),
        ),
    ]