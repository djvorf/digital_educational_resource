# Generated by Django 3.0.5 on 2020-04-03 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0002_auto_20200402_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lector',
            old_name='lectors/',
            new_name='lectorn/',
        ),
    ]