from django.contrib import admin
from teacherfeedback.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('surname', 'name', 'profile_type', 'mobile')

admin.site.register(Profile, ProfileAdmin)
