# Generated by Django 3.1.5 on 2021-01-13 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='password12',
            new_name='password2',
        ),
    ]
