# Generated by Django 5.1 on 2024-08-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
