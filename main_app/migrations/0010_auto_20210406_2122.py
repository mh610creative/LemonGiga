# Generated by Django 3.1.7 on 2021-04-06 21:22
from django.template.defaultfilters import slugify


from django.db import migrations

def populate_slug(apps, schema_editor):
    print('populating')
    Gear = apps.get_model('main_app', 'Gear')

    gears = Gear.objects.all()
    print('gears', gears)
    for gear in gears:
        slug = slugify(gear.name)
        gear.slug = slug[:50]
        gear.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_gear_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slug, migrations.RunPython.noop)
    ]
