# Generated by Django 4.0.4 on 2022-05-21 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelTable(
            name='students',
            table='students',
        ),
    ]
