from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

INCIDENT_TYPES = (
    ('Absent', 'Absent'),
    ('NoTeaching', 'No Teaching'),
    ('Abuse', 'Abuse'),
    ('Other', 'Other'),
)

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
    mobile = models.CharField(max_length=100, unique=True, help_text=_("The person's mobile phone number."))
    profile_type = models.CharField(max_length=30, choices=Profile.TYPES, default=Profile.STUDENT)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)

class School(models.Model):
    name = models.CharField(max_length=255, help_text=_("School's name"))
    street_number = models.IntegerField(help_text=_("School's street number"))
    street_name = models.CharField(max_length=255, help_text=_("School's street name"))
    city = models.IntegerField(help_text=_("School's city"))
    province = models.IntegerField(help_text=_("School's province"))
    country = models.IntegerField(help_text=_("School's country"))

class Grade(models.Model):
    number = models.IntegerField(help_text=_("Grade number"))

class Subject(models.Model):
    name = models.CharField(max_length=255, help_text=_("Name of a subject"))

class GradeSubject(models.Model):
    grade = models.ForeignKey(Grade)
    subject = models.ForeignKey(Subject)

class Rating(models.Model):
    value = models.IntegerField(help_text=_("Rating given to a teacher"))
    comment = models.CharField(max_length=1000, help_text=_("Comment associated with a rating"))
    teacher = models.ForeignKey(Profile)

class Incident(models.Model):
    incidentType = models.CharField(max_length=255, help_text=_("Type of incident"), choices=INCIDENT_TYPES)
    otherType = models.CharField(max_length=255, help_text=_("Other type of incident"), blank=True)
    comment = models.CharField(max_length=1000, help_text=_("Comment associated with a incident"))
    teacher = models.ForeignKey(Profile)
