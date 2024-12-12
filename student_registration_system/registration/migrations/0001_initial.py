# Generated by Django 5.1.2 on 2024-10-20 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_catalog', '0002_remove_course_created_at_alter_course_department_and_more'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_catalog.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.student')),
            ],
        ),
    ]