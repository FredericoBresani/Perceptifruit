# Generated by Django 4.2.20 on 2025-03-30 21:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_alter_fruitreading_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitreading',
            name='read',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
