# Generated by Django 4.2.19 on 2025-02-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website', '0006_remove_footerdata_copyright_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Event', 'Event'), ('News', 'News')], default='Event', max_length=10),
        ),
    ]
