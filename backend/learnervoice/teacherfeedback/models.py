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
    mobile = models.CharField(max_length=100, unique=True, help_text=_("The person's mobile phone number."))
    profile_type = models.CharField(max_length=30, choices=Profile.TYPES, default=Profile.STUDENT)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)

