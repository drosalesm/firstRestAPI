# Generated by Django 3.1.7 on 2022-10-07 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='create_at',
            new_name='created_at',
        ),
    ]