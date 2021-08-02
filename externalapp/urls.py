from django.urls import path
from externalapp import views


urlpatterns = [
    path("", views.index, name="home"),
    path("studentinfo", views.getStudentInfo, name="studentinfo"),
    path("allstudentsinfo", views.getAllStudentsInfo, name="allstudentsinfo"),
    path("poststudentinfo", views.postStudentInfo, name="poststudentinfo"),
    path("getstudent", views.getStudent, name="getstudent"),
    path("updatestudent", views.updateStudent, name="updatestudent"),
    path("deletestudent", views.deleteStudent, name="deletestudent"),
    path("getteacher", views.getTeacherData, name="getteacher"),
    path("postteacher", views.postTeacherData, name="postteacher"),
    path("putteacher", views.putTeacherData, name="putteacher"),
    path("patchteacher", views.patchTeacherData, name="patchteacher"),
    path("deleteteacher", views.deleteTeacherData, name="deleteteacher"),
    path("modelviewsetteacher", views.getModelViewsetTeacherData,
         name="modelviewsetteacher"),
    path("gettoken", views.GenerateToken,
         name="gettoken"),

]
