# Generated by Django 4.1.6 on 2023-04-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actapp', '0005_rename_email_id_operatorregister_operatoremail_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentors_name', models.CharField(max_length=100)),
                ('mentors_Designation', models.CharField(max_length=1000)),
                ('mentors_details', models.CharField(max_length=1000)),
                ('image', models.CharField(default='onimage.png', max_length=225)),
                ('registerdate', models.CharField(default='', max_length=100)),
                ('softdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='operatorregister',
            old_name='Operatorrole',
            new_name='role',
        ),
    ]