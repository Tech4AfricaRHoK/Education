from rest_framework.views import APIView
from rest_framework.response import Response
from teacherfeedback.models import Profile
from teacherfeedback.serializers import UserSerializer



class UsersAPI(APIView):
    """
    API for handling all user-related functionality.
    """

    def get(self, request, format=None):
        """
        GET request. This primarily allows us to fetch a list of teachers at present.
        """
        return Response([UserSerializer(
            id=user.id,
            name=user.name,
            surname=user.surname,
            profile_type=user.profile_type) \
            for user in Profile.objects.filter(profile_type=Profile.TEACHER).order_by('surname', 'name').all()])

