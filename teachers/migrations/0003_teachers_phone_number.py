# Generated by Django 4.0.4 on 2022-05-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teachers_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='phone_number',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
