# Generated by Django 4.2.19 on 2025-02-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website', '0013_alter_academicevent_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicevent',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
