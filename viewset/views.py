from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.


def viewSet(request):
    return HttpResponse("<h1>viewset</h1>")


class teacherViewset(viewsets.ViewSet):

    # to get list of all objects
    def list(self, request):
        try:
            teachers = Teacher.objects.all()
            serializer_result = teacherSerializer(teachers, many=True)
            return Response(serializer_result.data)
        except Exception as e:
            print(e)

    # to create teacher object
    def create(self, request):
        try:
            serializer_result = teacherSerializer(data=request.data)
            if serializer_result.is_valid():
                serializer_result.save()
                return Response(serializer_result.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_result.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

    # to fully update teacher object
    def update(self, request, pk=None):
        try:
            print("pk:", pk, "request data:", request.data)
            if Teacher.objects.filter(teacher_id=pk).exists():
                teacher_obj = Teacher.objects.get(teacher_id=pk)
                serializer_result = teacherSerializer(
                    teacher_obj, request.data)
                if serializer_result.is_valid():
                    serializer_result.save()
                    return Response(serializer_result.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer_result.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'msg': 'no data found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)

    # to partially update teacher object
    def partial_update(self, request, pk=None):
        try:
            print("pk:", pk, "request data:", request.data)
            if pk is None or Teacher.objects.filter(teacher_id=pk) is None:
                return Response({'msg': 'no data found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                teacher_obj = Teacher.objects.get(teacher_id=pk)
                serializer_result = teacherSerializer(
                    teacher_obj, request.data, partial=True)
                if serializer_result.is_valid():
                    serializer_result.save()
                    return Response(serializer_result.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer_result.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

    # to retrieve any teacher object
    def retrieve(self, request, pk=None):
        print(pk)
        if Teacher.objects.filter(teacher_id=pk).exists():
            teacher_obj = Teacher.objects.get(teacher_id=pk)
            serializer_result = teacherSerializer(teacher_obj)
            return Response(serializer_result.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'no data found'}, status=status.HTTP_404_NOT_FOUND)

    # to delete any teacher object
    def destroy(self, request, pk=None):
        if pk is None:
            return Response({'msg': 'no data found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            teacher_obj = Teacher.objects.get(teacher_id=pk)
            teacher_obj.delete()
            return Response({'msg': 'teacher data deleted'}, status=status.HTTP_200_OK)
