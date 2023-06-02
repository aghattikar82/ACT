# Generated by Django 4.1.6 on 2023-04-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=13)),
                ('email_id', models.CharField(max_length=100)),
                ('created_on', models.CharField(default='', max_length=100)),
                ('created_by', models.CharField(default='', max_length=100)),
                ('registerdate', models.CharField(default='', max_length=100)),
                ('softdelete', models.IntegerField(default=0)),
            ],
        ),
    ]
