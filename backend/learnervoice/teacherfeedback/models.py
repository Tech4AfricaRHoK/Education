from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Profile(models.Model):
    """
    Every user in the system has a profile, but not every profile has a user
    associated with it.
    """
    user = models.ForeignKey(User, blank=True, null=True,
            help_text=_("The (optional) user account associated with this profile."))
    name = models.CharField(max_length=255, help_text=_("The person's first name"))
    surname = models.CharField(max_length=255, help_text=_("The person's last name"))

