from rest_framework.views import APIView
from rest_framework.response import Response
from teacherfeedback.models import Profile



class UsersAPI(APIView):
    """
    API for handling all user-related functionality.
    """

    def get(self, request, format=None):
        """
        GET request. This primarily allows us to fetch a list of teachers at present.
        """
        return Profile.objects.filter(profile_type=Profile.TEACHER).order_by('surname', 'name').all()

