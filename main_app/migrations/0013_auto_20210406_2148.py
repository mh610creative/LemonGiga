# Generated by Django 3.1.7 on 2021-04-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20210406_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]