# Generated by Django 4.0.4 on 2022-04-15 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='student',
            new_name='is_student',
        ),
    ]
