# Generated by Django 3.1.7 on 2021-03-18 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_gear'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, null=True)),
                ('gear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.gear')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.person')),
            ],
        ),
    ]
