# Generated by Django 4.2.19 on 2025-02-15 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_website', '0027_alter_aboutpage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': 'About Page', 'verbose_name_plural': 'About Page'},
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='updated_at',
        ),
    ]
