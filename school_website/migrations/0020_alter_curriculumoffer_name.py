# Generated by Django 4.2.19 on 2025-02-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website', '0019_curriculumoffer_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculumoffer',
            name='name',
            field=models.CharField(choices=[('kindergarten', 'Kindergarten'), ('nursery', 'Nursery'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('islamiyya', 'Islamiyya'), ('nexora_digital', 'Nexora Digital Academy')], max_length=255, unique=True),
        ),
    ]
