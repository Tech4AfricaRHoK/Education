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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('incident_type', models.CharField(choices=[('absent', 'Absent'), ('notteaching', 'Not teaching'), ('abuse', 'Abuse'), ('missing', 'Missing teacher'), ('other', 'Other')], help_text='Type of incident', max_length=255)),
                ('other_type', models.CharField(null=True, help_text='Other type of incident', max_length=255, blank=True)),
                ('comment', models.TextField(null=True, help_text='Comment associated with a incident', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text="The person's first name", max_length=255)),
                ('surname', models.CharField(help_text="The person's last name", max_length=255)),
                ('mobile', models.CharField(unique=True, help_text="The person's mobile phone number.", max_length=100)),
                ('profile_type', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('parent', 'Parent'), ('principal', 'Principal'), ('admin', 'Admin')], max_length=30, default='student')),
                ('grade', models.IntegerField(null=True, help_text='The grade associated with this profile, if any', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('value', models.IntegerField(help_text='Rating given to a teacher')),
                ('comment', models.TextField(null=True, help_text='Comment associated with a rating', blank=True)),
                ('student', models.ForeignKey(related_name='student_ratings', help_text='The student associated with this rating', to='teacherfeedback.Profile')),
                ('teacher', models.ForeignKey(related_name='teacher_ratings', help_text='The teacher associated with this rating', to='teacherfeedback.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text="School's name", max_length=255)),
                ('street_number', models.IntegerField(help_text="School's street number")),
                ('street_name', models.CharField(help_text="School's street name", max_length=255)),
                ('city', models.IntegerField(help_text="School's city")),
                ('province', models.IntegerField(help_text="School's province")),
                ('country', models.IntegerField(help_text="School's country")),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, help_text='Name of a subject', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubjectGrade',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
            field=models.ForeignKey(blank=True, to='teacherfeedback.School', help_text='The school for this user, if any', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, help_text='The (optional) user account associated with this profile.', null=True),
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
