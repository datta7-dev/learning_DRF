from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
# Create your views here.


def genericApiViews(request):
    return HttpResponse("<h1>generic api views</h1>")


class listTeacher(ListAPIView):
    try:
        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer
    except Exception as e:
        print(e)


class createTeacher(CreateAPIView):
    try:
        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer
    except Exception as e:
        print(e)


class retrieveTeacher(RetrieveAPIView):
    try:
        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer
    except Exception as e:
        print(e)


class updateTeacher(UpdateAPIView):
    try:
        serializer_class = teacherSerializer

        def get_queryset(self):  # or queryset=Teacher.objects.all()
            return Teacher.objects.all()

    except Exception as e:
        print(e)


class destroyTeacher(DestroyAPIView):
    try:
        serializer_class = teacherSerializer

        def get_queryset(self):  # or queryset=Teacher.objects.all()
            return Teacher.objects.all()

    except Exception as e:
        print(e)
