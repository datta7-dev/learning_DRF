from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def modelViewset(request):
    return HttpResponse("<h1>model viewset</h1>")


# model viewset automatically uses list,create,put,patch,retrieve,destroy as per request made by user
""" class teacherModelViewset(viewsets.ModelViewSet):
    try:

        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer

    except Exception as e:
        print(e)
 """


# read only model viewset automatically uses list and retrieve only as per request
class readOnlyTeacherModelViewset(viewsets.ReadOnlyModelViewSet):
    try:
        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer
        authentication_classes = [TokenAuthentication]
        # to use this token authentication use this url from httpi from command line: http GET...POST,PUT,DELETE,PATCH http://127.0.0.1:8000/modelviewset/modelviewsetmodelviewset/ parameter1=value parameter2=value parameter_n=value 'Authorization: Token 29865ce0fa1345e1b6eee4937bf4c577e28f18da'
        permission_classes = [IsAuthenticated]
    except Exception as e:
        print(e)
