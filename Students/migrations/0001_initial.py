# Generated by Django 5.1.4 on 2025-01-11 05:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50, verbose_name='Province')),
                ('district', models.CharField(max_length=50, verbose_name='District')),
                ('local_body', models.CharField(max_length=50, verbose_name='Local Body')),
                ('ward', models.CharField(max_length=10, verbose_name='Ward')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='GuardianInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=255, verbose_name="Father's Name")),
                ('mother_name', models.CharField(max_length=255, verbose_name="Mother's Name")),
                ('guardian_name', models.CharField(max_length=255, verbose_name="Guardian's Name")),
            ],
            options={
                'verbose_name': 'Guardian Info',
                'verbose_name_plural': 'Guardian Infos',
            },
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, verbose_name='Gender')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Enter a valid phone number (up to 15 digits).')], verbose_name='Phone Number')),
                ('nationality', models.CharField(max_length=50, verbose_name='Nationality')),
            ],
            options={
                'verbose_name': 'Personal Info',
                'verbose_name_plural': 'Personal Infos',
            },
        ),
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='Admin.faculty')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='Admin.grade')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='Admin.level')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majors', to='Admin.major')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='Admin.section')),
            ],
            options={
                'verbose_name': 'Academic Info',
                'verbose_name_plural': 'Academic Infos',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academic_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='Students.academicinfo')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='Students.address')),
                ('guardian_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='Students.guardianinfo')),
                ('person_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='Students.personinfo')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]