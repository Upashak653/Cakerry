# Generated by Django 5.1.1 on 2024-09-26 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0004_rename_description_feedback_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='description',
            new_name='Description',
        ),
    ]
