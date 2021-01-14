# Generated by Django 3.1.5 on 2021-01-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210113_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=200, null=True)),
                ('password2', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
