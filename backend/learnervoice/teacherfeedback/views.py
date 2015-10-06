from teacherfeedback.models import Profile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json


def ser(o):
    """
    Shortcut for serialization.
    """
    return json.dumps(o)


def err(msg):
    """
    Shortcut for error handling.
    """
    return ser({"error": msg})


def json_response(r):
    return HttpResponse(ser(r), content_type='application/json')


def json_err(msg, code):
    response = HttpResponse(err(msg), content_type='application/json')
    response.status_code = code
    return response


def list_teachers(request):
    """
    Provides a listing of all of the teachers.
    """
    if 'q' in request.GET:
        query = request.GET['q']
        print("Attempting to query teachers by search string: %s" % query)
        return json_response([p for p in Profile.objects.filter( \
            profile_type=Profile.TEACHER).filter(Q(name__icontains=query) | Q(surname__icontains=query)).all()])
    else:
        return json_response([p for p in Profile.objects.filter( \
            profile_type=Profile.TEACHER).all()])


def add_user(request):
    """
    Allows us to add a user.
    """
    obj = None
    # first we need to validate the request
    try:
        obj = json.loads(request.body.decode('utf-8'))
        print(obj)
    except Exception as e:
        return json_err("Invalid request body: %s" % e, 400)

    return json_response(obj)


def rate_teacher(request):
    """
    Allows a student to rate a teacher.
    """
    pass


@csrf_exempt
def manage_users(request):
    """
    Primary function for managing our users.
    """
    if request.method == 'GET':
        return list_teachers(request)
    elif request.method == 'POST':
        return add_user(request)

    return json_err("Method not allowed", 405)

