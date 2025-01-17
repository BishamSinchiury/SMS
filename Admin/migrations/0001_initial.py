# Generated by Django 5.1.4 on 2025-01-11 05:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the faculty, e.g., Science, Arts, Commerce, etc.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(blank=True, help_text='Optional description of the faculty', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the educational level, e.g., Primary, Secondary, etc.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(blank=True, help_text='Optional description of the level', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Grade name or identifier, e.g., Grade 1, Grade 10, etc.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level', models.ForeignKey(help_text='Level this grade belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='Admin.level')),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Section name or identifier, e.g., A, B, etc.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grade', models.ForeignKey(help_text='Grade this section belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='Admin.grade')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the subject, e.g., Mathematics, Physics, etc.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('code', models.CharField(help_text='Unique code for the subject, e.g., MATH101', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(help_text='Faculty this subject belongs to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects', to='Admin.faculty')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the major, e.g., Computer Science, Biology, etc.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(blank=True, help_text='Optional description of the major', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subjects', models.ManyToManyField(help_text='Subjects included in this major', related_name='majors', to='Admin.subject')),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
            },
        ),
    ]
