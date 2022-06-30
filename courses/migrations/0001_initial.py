# Generated by Django 4.0.4 on 2022-06-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count_students', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'db_table': 'courses',
            },
        ),
    ]
