from django.urls import path, include
from mainapi import views
urlpatterns = [
    path("getstudent/<int:rn>", views.getStudent, name="getstudent"),
    path("getallstudents", views.getAllStudents, name="getallstudents"),
    path("poststudent", views.postStudent, name="poststudent"),
    path("getstudentdata", views.getStudentData, name="getstudentdata"),
    path("updatestudentdata", views.updateStudentData, name="updatestudentdata"),
    path("deletestudentdata", views.deleteStudentData, name="deletestudentdata")
]
