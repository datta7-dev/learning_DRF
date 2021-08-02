from django.shortcuts import render
from django.http import HttpResponse
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

""" there are multiple ways to generate token:-
    -mention rest_framework.authtoken in INSTALLED_APPS in settings.py file.
    -then run makemigration and migrate commands.
    way 1-create directly from django admin panel.
    way 2-using command line,syntax- python manage.py drf_create_token username
    way 3-by exposing api end point:
        -drf provides built in url for this.
        -syntax for creating token,
        from rest_framework.authtoken.views import obtain_auth_token
        urlpatterns=[path('gettoken/',obtain_auth_token)]
        -syntax for sending request to create token,
        http POST http://127.0.0.1:8000/gettoken/ username="" password=""
        it uses http post request to send request with username and password for creating token.
        if username and password is valid then it generates and returns token in json response.
    way 3- by using signals.
"""

""" note: whichever authentication type we have used it is must to use permission classes after authentication.
"""


def tokenAuthHome(request):
    return HttpResponse("welcome token authentication")
