from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
# Create your views here.

# defualt called fuctio
#
# def delete(self,request,*args,**kwargs):
# return self.destroy(request,*args,**kwargs)n


def genericMixins(request):
    return HttpResponse("<h1>mixins and generic api view</h1>")


# returns all the objects from model
class listTeacher(GenericAPIView, ListModelMixin):
    try:

        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    except Exception as e:
        print(e)


# creates new object and save it
class createTeacher(GenericAPIView, CreateModelMixin):
    try:

        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)

    except Exception as e:
        print(e)


# update teacher by teacher id
class updateTeacher(GenericAPIView, UpdateModelMixin):
    try:

        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        """def patch(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs) """

    except Exception as e:
        print(e)


# get teacher by teacher id
class getTeacher(GenericAPIView, RetrieveModelMixin):
    try:

        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

    except Exception as e:
        print(e)


# delete teacher by teacher id
class destroyTeacher(GenericAPIView, DestroyModelMixin):
    try:

        queryset = Teacher.objects.all()
        serializer_class = teacherSerializer

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)

    except Exception as e:
        print(e)
