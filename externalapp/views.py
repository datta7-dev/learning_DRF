from django.shortcuts import render, HttpResponse
import json
import requests
import random
# Create your views here.


# default method for external app
def index(request):
    return HttpResponse("external app")


# call api to get student info
def getStudentInfo(request):
    try:
        # api url
        url = "http://127.0.0.1:8000/api/getstudent/1"
        # call api url
        return_students_result = requests.get(url=url)
        # extracts json from response
        students_data = return_students_result.json()
        print(students_data)
        data = (students_data.get('roll_no'), " ", students_data.get(
            'name'), "  ", students_data.get('marks'))
        return HttpResponse(data)
    except Exception as e:
        print(e)


def getAllStudentsInfo(request):
    try:
        url = "http://127.0.0.1:8000/api/getallstudents"
        return_students_result = requests.get(url=url)
        students_data = return_students_result.json()
        print(len(students_data))
        print(students_data)
        return HttpResponse(students_data)
    except Exception as e:
        print(e)


def postStudentInfo(request):
    try:
        python_data = {
            'roll_no': random.randint(10, 100),
            'name': "student"+str(random.randint(10, 100)),
            'marks': random.randint(10, 150),
        }
        # print(python_data)
        json_data = json.dumps(python_data)
        # print(json_data)
        url = "http://127.0.0.1:8000/api/poststudent"
        return_result = requests.post(url=url, data=json_data)
        print(return_result.json())
        return HttpResponse("ok")
    except Exception as e:
        print(e)


# get student info by specific value
def getStudent(request):
    try:
        python_data = {
            'roll_no': 1,
        }
        # print(python_data)
        json_data = json.dumps(python_data)
        # print(json_data)
        url = "http://127.0.0.1:8000/api/getstudentdata"
        return_result = requests.get(url=url, data=json_data)
        print(return_result.json())
        return HttpResponse("ok")
    except Exception as e:
        print(e)


def updateStudent(request):
    data = {
        'roll_no': 1,
        'name': "student21",
        'marks': 77,
    }
    json_data = json.dumps(data)
    url = "http://127.0.0.1:8000/api/updatestudentdata"
    return_result = requests.put(url=url, data=json_data)
    print(return_result.json())
    return HttpResponse("update done")


def deleteStudent(request):
    data = {
        'roll_no': 19
    }
    json_data = json.dumps(data)
    url = "http://127.0.0.1:8000/api/deletestudentdata"
    return_result = requests.delete(url=url, data=json_data)
    print(return_result.json())
    return HttpResponse("done")


# api view for teacher
# get teacher data
def getTeacherData(request):
    try:
        data = {
            'teacher_id': 14,
        }
        json_data = json.dumps(data)
        url = "http://127.0.0.1:8000/apiview/getteacher"
        headers = {
            'content-Type': 'application/json',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2OTU1MTcwLCJqdGkiOiJlOTM1MGJhZjc3NDk0NGJiYmUxN2M3OGIzMTM1MTVmYiIsInVzZXJfaWQiOjJ9.nDReWTw3dC3Lzg8XdTiGIeGtc6ELRtrx_WDljPo19Gw'

        }
        return_result = requests.get(url=url, headers=headers, data=json_data)
        print(return_result.json())
        return HttpResponse(return_result.json().get('msg'))
    except Exception as e:
        print(e)


# post teacher data
def postTeacherData(request):
    try:
        data = {
            'teacher_id': random.randint(10, 100),
            'name': "teacher" + str(random.randint(10, 100)),
        }
        json_data = json.dumps(data)
        # for api view need to mention which type of data which we are sending.
        headers = {'content-Type': 'application/json'}
        url = "http://127.0.0.1:8000/apiview/postteacher"
        return_result = requests.post(url=url, headers=headers, data=json_data)
        print(return_result.json())
        return HttpResponse(return_result.json().get('msg'))
    except Exception as e:
        print(e)


def putTeacherData(request):
    try:

        data = {
            'teacher_id': 30,
            'name': "teacher99",
        }
        json_data = json.dumps(data)

        url = "http://127.0.0.1:8000/apiview/putteacher"
        headers = {
            'content-Type': 'application/json',
        }

        return_result = requests.put(url=url, headers=headers, data=json_data)
        print(return_result.json())

        return HttpResponse(return_result.json())

    except Exception as e:
        print(e)


def patchTeacherData(request):
    try:

        data = {
            'teacher_id': 1,
            'name': 'teacher'+str(random.randint(50, 100)),
        }
        json_data = json.dumps(data)

        headers = {
            'content-Type': 'application/json',
        }

        url = "http://127.0.0.1:8000/apiview/patchteacher"

        return_result = requests.patch(
            url=url, headers=headers, data=json_data)

        print(return_result.json())
        return HttpResponse(return_result.json())

    except Exception as e:
        print(e)


def deleteTeacherData(request):
    try:

        data = {
            'teacher_id': 2,
        }
        json_data = json.dumps(data)

        url = "http://127.0.0.1:8000/apiview/deleteteacher"
        headers = {
            'content-Type': 'application/json'
        }
        return_result = requests.delete(
            url=url, headers=headers, data=json_data)
        print(return_result.json())
        return HttpResponse(return_result.json())

    except Exception as e:
        print(e)


# get teacher data from model viewset
def getModelViewsetTeacherData(request):
    try:
        data = {
            'teacher_id': 1,
        }
        json_data = json.dumps(data)
        url = "http://127.0.0.1:8000/modelviewset/modelviewsetmodelviewset/"
        headers = {
            'content-Type': 'application/json'
        }
        return_result = requests.get(url=url, headers=headers)
        print(return_result.json())
        return HttpResponse(return_result.json())
    except Exception as e:
        print(e)


# request to generate token
def GenerateToken(request):
    try:
        url = "http://127.0.0.1:8000/tokenauthentication/gettoken"
        headers = {
            'content-type': 'application/json',
        }
        data = {
            'username': 'datta',
            'password': 'datta7'
        }
        json_data = json.dumps(data)
        return_data = requests.post(url=url, headers=headers, data=json_data)
        print(return_data.json())
        print(return_data.json().get('token'),
              len(return_data.json().get('token')))
        return HttpResponse("token generated")
    except Exception as e:
        print(e)
