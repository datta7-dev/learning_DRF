from django.shortcuts import render, HttpResponse
from mainapi.models import Student
# , updateStudentSerializer, postStudentSerializer, getStudentDataSerializer
from mainapi.serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.


# get single student object as json data
def getStudent(request, rn):
    try:
        # get single object from database
        student = Student.objects.get(roll_no=rn)
        # pass object to serializer which converts object data into python dictionary data
        student_serialized_data = studentSerializer(student)
        # print(student_serialized_data.data)
        # json renderer converts serialized data(python data) into json format
        student_json_data = JSONRenderer().render(student_serialized_data.data)
        # print(student_json_data)
        return HttpResponse(student_json_data, content_type="application/json")
    except Exception as e:
        print(e)

    # json.dumps(python dict) converts python dict data into json format as shown below
    # and json.loads(json data) converts json data into python dict format as shown below
    # json_data = json.dumps(student_serialized_data.data)
    # print(json.loads(json_data))


# get all student object as json data
def getAllStudents(request):
    try:
        # get single object from database
        student = Student.objects.all()
        # pass object to serializer which converts object data into python dictionary data
        student_serialized_data = studentSerializer(
            student, many=True)  # use many=True if it has multiple objects
        # print(student_serialized_data.data)
        # json renderer converts serialized data(python data) into json format
        # student_json_data = JSONRenderer().render(student_serialized_data.data)
        # print(student_json_data)
        # return HttpResponse(student_json_data, content_type="application/json")

        # ===OR====
        # instead of JSONRenderer and HttpResponse we can simply use JsonResponse
        # to allow non dict data keep safe=False, for single serialized object it is an dict data but in case multiple serialized objects are list of objects.
        return JsonResponse(student_serialized_data.data, safe=False)

    except Exception as e:
        print(e)


# post student data
@csrf_exempt
def postStudent(request):
    try:
        if request.method == "POST":
            json_data = request.body
            # print(json_data)
            stream = io.BytesIO(json_data)
            # print(stream)
            parse_python_data = JSONParser().parse(stream)
            serializer_result = studentSerializer(data=parse_python_data)
            if serializer_result.is_valid():
                serializer_result.save()
                return_msg = {
                    'msg': "object created successfully",
                }
                return_data = JSONRenderer().render(return_msg)
                # print(return_data)
                return HttpResponse(return_data, content_type="application/json")
            else:
                return_data = JSONRenderer().render(serializer_result.errors)
                return HttpResponse(return_data, content_type="application/json")

    except Exception as e:
        print(e)


# get student data
def getStudentData(request):
    try:
        if request.method == "GET":
            json_data = request.body
            stream = io.BytesIO(json_data)
            parse_python_data = JSONParser().parse(stream)
            # print(parse_python_data)
            rn = parse_python_data.get('roll_no')
            if Student.objects.filter(roll_no=rn).exists():
                data_object = Student.objects.get(
                    roll_no=rn)
                serializer_result = studentSerializer(data_object)
                # print(serializer_result)
                json_data = json.dumps(serializer_result.data)
                # return HttpResponse(json_data, content_type="application/json")
                return JsonResponse(serializer_result.data, safe=True)
            else:
                return_data = {
                    'msg': "no data found"
                }
                return JsonResponse(return_data, safe=True)
    except Exception as e:
        print(e)


# update student data
@csrf_exempt
def updateStudentData(request):
    try:
        if request.method == "PUT":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            rn = python_data.get('roll_no')
            obj = Student.objects.get(
                roll_no=rn)
            serializer_result = studentSerializer(
                obj, data=python_data, partial=True)
            if serializer_result.is_valid():
                serializer_result.save()
                print(serializer_result.data)
                response = {
                    'msg': "data updated successfully"
                }
                json_response = JSONRenderer().render(response)
                return HttpResponse(json_response, content_type="application/json")
            else:
                json_response = JSONRenderer().render(serializer_result.errors)
                return HttpResponse(json_response, content_type="application/json")
    except Exception as e:
        print(e)


# to delete data
@csrf_exempt
def deleteStudentData(request):
    try:
        if request.method == "DELETE":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            print(python_data)
            rn = python_data.get('roll_no')
            student_obj = Student.objects.get(roll_no=rn)
            student_obj.delete()
            response_data = {
                'msg': "data deleted successfully"
            }
            json_response = JSONRenderer().render(response_data)
            return HttpResponse(json_response, content_type="application/json")
    except Exception as e:
        print(e)
