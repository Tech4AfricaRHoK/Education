from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _



class Profile(models.Model):
    """
    Every user in the system has a profile, but not every profile has a user
    associated with it.
    """
    STUDENT = 'student'
    TEACHER = 'teacher'
    PARENT = 'parent'
    PRINCIPAL = 'principal'
    ADMIN = 'admin'

    TYPES = (
        (STUDENT, _('Student')),
        (TEACHER, _('Teacher')),
        (PARENT, _('Parent')),
        (PRINCIPAL, _('Principal')),
        (ADMIN, _('Admin')),
    )

    user = models.ForeignKey(User, blank=True, null=True,
            help_text=_("The (optional) user account associated with this profile."))
    name = models.CharField(max_length=255, help_text=_("The person's first name"))
    surname = models.CharField(max_length=255, help_text=_("The person's last name"))
    mobile = models.CharField(max_length=100, null=True, blank=True, help_text=_("The person's mobile phone number."))
    profile_type = models.CharField(max_length=30, choices=TYPES, default=STUDENT)
    school = models.ForeignKey('School', null=True, blank=True, help_text=_("The school for this user, if any"))
    grade = models.IntegerField(null=True, blank=True, help_text=_("The grade associated with this profile, if any"))

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class School(models.Model):
    name = models.CharField(max_length=255, help_text=_("School's name"))
    street_number = models.IntegerField(help_text=_("School's street number"))
    street_name = models.CharField(max_length=255, help_text=_("School's street name"))
    city = models.CharField(max_length=255, help_text=_("School's city"))
    province = models.CharField(max_length=255, help_text=_("School's province"))
    country = models.CharField(max_length=255, help_text=_("School's country"))

    def __unicode__(self):
        return "%s" % self.name


class Subject(models.Model):
    name = models.CharField(max_length=255, help_text=_("Name of a subject"), unique=True)

    def __unicode__(self):
        return self.name


class TeacherSubjectGrade(models.Model):
    """
    A particular subject taught by a particular teacher, for a specific grade and school.
    """
    teacher = models.ForeignKey(Profile)
    subject = models.ForeignKey(Subject)
    grade = models.IntegerField()
    year = models.IntegerField(help_text=_("The year for which this subject is relevant"))
    school = models.ForeignKey(School)


class Rating(models.Model):
    """
    For when a student wants to rate a particular teacher.
    """
    value = models.IntegerField(help_text=_("Rating given to a teacher"))
    comment = models.TextField(blank=True, null=True, help_text=_("Comment associated with a rating"))
    teacher = models.ForeignKey(Profile, help_text=_("The teacher associated with this rating"), related_name='teacher_ratings')
    student = models.ForeignKey(Profile, help_text=_("The student associated with this rating"), related_name='student_ratings')


class Incident(models.Model):
    """
    For when a student wants to report some kind of incident involving a teacher.
    """
    ABSENT = 'absent'
    MISSING_TEACHER = 'missing'
    NOT_TEACHING = 'notteaching'
    ABUSE = 'abuse'
    OTHER = 'other'

    TYPES = (
        (ABSENT, 'Absent'),
        (NOT_TEACHING, 'Not teaching'),
        (ABUSE, 'Abuse'),
        (MISSING_TEACHER, 'Missing teacher'),
        (OTHER, 'Other'),
    )
    incident_type = models.CharField(max_length=255, help_text=_("Type of incident"), choices=TYPES)
    other_type = models.CharField(max_length=255, help_text=_("Other type of incident"), blank=True, null=True)
    comment = models.TextField(blank=True, null=True, help_text=_("Comment associated with a incident"))
    teacher = models.ForeignKey(Profile, help_text=_("The teacher associated with this incident"), related_name='teacher_incidents')
    student = models.ForeignKey(Profile, help_text=_("The student associated with this incident"), related_name='student_incidents')
