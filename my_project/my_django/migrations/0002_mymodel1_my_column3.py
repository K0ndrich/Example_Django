# Generated by Django 5.1 on 2024-08-22 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel1',
            name='my_column3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='my_django.mymodel2'),
        ),
    ]
