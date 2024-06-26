# Generated by Django 5.0.3 on 2024-03-25 07:59

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.models.MyUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, help_text="Designates whether this user's email is verified. ", verbose_name='email_verified'),
        ),
    ]
