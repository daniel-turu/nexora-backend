# Generated by Django 4.2.19 on 2025-02-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website', '0009_alter_event_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Exam', 'Exam'), ('Lecture', 'Lecture'), ('Holiday', 'Holiday'), ('Workshop', 'Workshop'), ('Meeting', 'Meeting'), ('Other', 'Other')], default='Other', max_length=20)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='academic_events/')),
            ],
        ),
    ]
