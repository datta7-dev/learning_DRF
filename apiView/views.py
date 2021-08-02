from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiView.models import Teacher
from apiView.serializers import teacherSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


def apiView(request):
    return HttpResponse("<h1>api view</h1>")


# use of function based api view.
# by default api_view contains get request, no need to mention GET.
# @api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
# @authentication_classes = []
# @permission_classes = []
"""
def teacherData(request):
    try:

        if request.method == 'GET':
            print(request.data)  # request.data contains parsed python data.
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            serializer_result = teacherSerializer(teacher_obj)
            print(serializer_result.data)
            response_data = {
                'msg': 'api view get teacher successfull',
                'data': serializer_result.data,
            }
            # Response can return python data, it contains native python data type e.g. python dict, variable. It sends data json
            return Response(response_data)

        if request.method == 'POST':
            print(request.data)  # request.data contains parsed python data.
            serializer_result = teacherSerializer(data=request.data)
            if serializer_result.is_valid():
                serializer_result.save()
                response_data = {
                    'msg': 'api view post teacher successfull',
                    'data': serializer_result.data,
                }
                # Response can return python data, it contains native python data type e.x. python dict, variable. It sends data json
                return Response(response_data)
            else:
                response_data = {
                    'msg': 'api view post teacher failed',
                    'data': serializer_result.errors,
                }
                # Response can return python data, it contains native python data type e.x. python dict, variable. It sends data json
                return Response(response_data)

        if request.method == "PUT":
            print(request.data)
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            print(teacher_obj.teacher_id)
            serializer_result = teacherSerializer(teacher_obj, request.data)
            print(serializer_result)
            if serializer_result.is_valid():
                serializer_result.save()
                response_data = {
                    'msg': 'data updated successfully',
                    'data': serializer_result.data,
                }
                return Response(response_data)
            else:
                response_data = {
                    'msg': 'api view put teacher failed',
                    'data': serializer_result.errors,
                }
                # Response can return python data, it contains native python data type e.x. python dict, variable. It sends data json
                return Response(response_data)

        if request.method == "PATCH":
            print(request.data)
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            serializer_result = teacherSerializer(
                teacher_obj, request.data, partial=True)
            if serializer_result.is_valid():
                serializer_result.save()
                response_data = {
                    'msg': "patch data successfull",
                    'data': serializer_result.data
                }
                return Response(response_data)
            else:
                response_data = {
                    'msg': "patch data successfull",
                    'data': serializer_result.errors
                }
                return Response(response_data)

        if request.method == "DELETE":
            print(request.data)
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            teacher_obj.delete()
            response_data = {
                'msg': "data deleted successfully",
            }
            return Response(response_data)

    except Exception as e:
        print(e)
 """


# use of class based api view
class teacherData(APIView):
    """ adding authorizaion and permission classes in apiview """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            # print(request.data)
            if Teacher.objects.filter(teacher_id=request.data.get('teacher_id')).exists():
                teacher_obj = Teacher.objects.get(
                    teacher_id=request.data.get('teacher_id'))
                serializer_result = teacherSerializer(teacher_obj)
                response_data = {
                    'msg': 'api view get data successfully',
                    'data': serializer_result.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'msg': 'api view get data failed',
                    'data': None
                }
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)

    def post(self, request, format=None):
        try:
            print(request.data)
            serializer_result = teacherSerializer(data=request.data)
            if serializer_result.is_valid():
                serializer_result.save()
                response_data = {
                    'msg': 'api view post data successfully',
                    'data': serializer_result.data
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {
                    'msg': 'api view post data failed',
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

    def put(self, request, format=None):
        try:
            print(request.data)
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            serializer_result = teacherSerializer(
                teacher_obj, data=request.data)
            if serializer_result.is_valid():
                serializer_result.save()
                response_data = {
                    'msg': 'api view put data successfully',
                    'data': serializer_result.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'msg': 'api view put data failed',
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

    def patch(self, request, format=None):
        try:
            print(request.data)
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            serializer_result = teacherSerializer(
                teacher_obj, data=request.data, partial=True)
            if serializer_result.is_valid():
                serializer_result.save()
                response_data = {
                    'msg': 'api view patch data successfully',
                    'data': serializer_result.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'msg': 'api view patch data failed',
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

    def delete(self, request, format=None):
        try:
            print(request.data)
            teacher_obj = Teacher.objects.get(
                teacher_id=request.data.get('teacher_id'))
            teacher_obj.delete()
            response_data = {
                'msg': 'api view delete data successfully',
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
