# Generated by Django 5.1.1 on 2024-10-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0008_book_cake_cake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
