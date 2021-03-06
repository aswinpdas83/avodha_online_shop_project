# Generated by Django 4.0.4 on 2022-06-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_users_usersdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('mob', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UsersDB',
        ),
    ]
