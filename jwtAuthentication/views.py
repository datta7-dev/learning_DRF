from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


def jwtHome(request):
    return HttpResponse("<h1>JWT Authentication</h1>")


# class based api view with jwt authentication
"""
api url syntax to access api with JWTAuthentication:  
http http://127.0.0.1:8000/jwtauthentication/teacherdata "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2OTIyMzc1LCJqdGkiOiJhMzI3MzhmNmRmOTY0NzE3YTVmMjJhZGY2OTc0ZWU1NyIsInVzZXJfaWQiOjJ9.MMlOQBbqlbssVe4cWdg-vmegs2ulPQtzDv6odVneAnQ" 
"""


class teacherData(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = teacherSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
