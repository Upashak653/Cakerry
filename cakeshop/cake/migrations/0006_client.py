# Generated by Django 5.1.1 on 2024-09-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0005_rename_description_aboutus_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]