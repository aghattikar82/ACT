# Generated by Django 4.1.6 on 2023-04-05 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actapp', '0003_operatorregister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatorregister',
            old_name='mobilenumber',
            new_name='mobile_number',
        ),
    ]
