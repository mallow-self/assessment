# Generated by Django 5.1.7 on 2025-03-17 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoTable',
            new_name='Todo',
        ),
    ]
