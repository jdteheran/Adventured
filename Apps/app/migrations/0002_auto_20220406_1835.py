# Generated by Django 2.2.8 on 2022-04-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='lenguaje',
            new_name='language',
        ),
    ]
