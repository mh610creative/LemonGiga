# Generated by Django 3.1.7 on 2021-03-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
