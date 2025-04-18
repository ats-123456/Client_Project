# Generated by Django 5.2 on 2025-04-17 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('staff', 'Staff'), ('hod', 'HOD')], max_length=10)),
                ('staff_id', models.CharField(blank=True, max_length=20, null=True)),
                ('hod_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=30)),
                ('section', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], default='a', max_length=30)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.classroom')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('cname', 'year', 'section'), name='unique_class_year_section')],
            },
        ),
    ]
