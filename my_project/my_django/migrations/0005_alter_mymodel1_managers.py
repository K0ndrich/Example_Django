# Generated by Django 5.1 on 2024-08-24 08:45

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_django', '0004_rename_my_column4_mymodel1_is_published_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='mymodel1',
            managers=[
                ('my_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
