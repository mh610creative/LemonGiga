# Generated by Django 3.1.7 on 2021-03-21 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210321_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gear',
            old_name='profile_pic',
            new_name='pack_shot',
        ),
    ]