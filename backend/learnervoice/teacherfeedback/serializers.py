"""
Serializers for the teacher feedback API.
"""

from teacherfeedback.models import Profile
from rest_framework import serializers


class TeacherSubjectSerializer(serializers.Serializer):
    """
    Allows us to serialize/deserialize the grades/subjects that a teacher teaches.
    """
    grade = serializers.IntegerField(required=True, min_value=1, max_value=12)
    subject = serializers.CharField(required=True, max_length=255)


class UserSerializer(serializers.Serializer):
    """
    Serializer for the different types of users.
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    surname = serializers.CharField(required=True, max_length=255)
    mobile = serializers.CharField(required=False, allow_null=True, max_length=100)
    password = serializers.CharField(max_length=255, required=False, allow_null=True)
    profile_type = serializers.ChoiceField(choices=Profile.TYPES, default=Profile.STUDENT)
    email = serializers.EmailField(required=False, max_length=255, allow_null=True)

    # for when we're creating a teacher - we need a subject list of what they teach
    subjects = serializers.ListField(
        child=TeacherSubjectSerializer(),
        required=False,
        allow_null=True
    )

    # for when we're creating a student and/or teacher - the pk of the school
    school_id = serializers.IntegerField(required=False, allow_null=True)
    # for when we're creating students
    grade = serializers.IntegerField(required=False, allow_null=True, min_value=1, max_value=12)


    def validate(self, data):
        """
        Checks if the data we've received is actually valid.
        """
        # if we're adding a student here
        if data['profile_type'] == Profile.STUDENT:
            if 'mobile' not in data or \
                    'password' not in data or \
                    'school' not in data or \
                    'grade' not in data:
                raise serializers.ValidationError("Missing field(s) in incoming request")

        elif data['profile_type'] == Profile.TEACHER:
            if 'mobile' in data:
                if 'password' not in data or 'subjects' not in data:
                    raise serializers.ValidationError("Missing field(s) in incoming request")

        return data


