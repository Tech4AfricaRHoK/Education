# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('incident_type', models.CharField(help_text='Type of incident', max_length=255, choices=[('absent', 'Absent'), ('notteaching', 'Not teaching'), ('abuse', 'Abuse'), ('missing', 'Missing teacher'), ('other', 'Other')])),
                ('other_type', models.CharField(blank=True, help_text='Other type of incident', null=True, max_length=255)),
                ('comment', models.TextField(blank=True, help_text='Comment associated with a incident', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(help_text="The person's first name", max_length=255)),
                ('surname', models.CharField(help_text="The person's last name", max_length=255)),
                ('mobile', models.CharField(blank=True, help_text="The person's mobile phone number.", null=True, max_length=100)),
                ('profile_type', models.CharField(max_length=30, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('parent', 'Parent'), ('principal', 'Principal'), ('admin', 'Admin')], default='student')),
                ('grade', models.IntegerField(blank=True, help_text='The grade associated with this profile, if any', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.IntegerField(help_text='Rating given to a teacher')),
                ('comment', models.TextField(blank=True, help_text='Comment associated with a rating', null=True)),
                ('student', models.ForeignKey(related_name='student_ratings', help_text='The student associated with this rating', to='teacherfeedback.Profile')),
                ('teacher', models.ForeignKey(related_name='teacher_ratings', help_text='The teacher associated with this rating', to='teacherfeedback.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(help_text="School's name", max_length=255)),
                ('street_number', models.IntegerField(help_text="School's street number")),
                ('street_name', models.CharField(help_text="School's street name", max_length=255)),
                ('city', models.CharField(help_text="School's city", max_length=255)),
                ('province', models.CharField(help_text="School's province", max_length=255)),
                ('country', models.CharField(help_text="School's country", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(help_text='Name of a subject', unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubjectGrade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('grade', models.IntegerField()),
                ('year', models.IntegerField(help_text='The year for which this subject is relevant')),
                ('school', models.ForeignKey(to='teacherfeedback.School')),
                ('subject', models.ForeignKey(to='teacherfeedback.Subject')),
                ('teacher', models.ForeignKey(to='teacherfeedback.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(null=True, blank=True, help_text='The school for this user, if any', to='teacherfeedback.School'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, blank=True, help_text='The (optional) user account associated with this profile.', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incident',
            name='student',
            field=models.ForeignKey(related_name='student_incidents', help_text='The student associated with this incident', to='teacherfeedback.Profile'),
        ),
        migrations.AddField(
            model_name='incident',
            name='teacher',
            field=models.ForeignKey(related_name='teacher_incidents', help_text='The teacher associated with this incident', to='teacherfeedback.Profile'),
        ),
    ]
