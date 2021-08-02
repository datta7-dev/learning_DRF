from django.urls import path, include
from apiView import views
urlpatterns = [
    path("", views.apiView, name="apiview"),
    path("getteacher", views.teacherData.as_view(), name="getteacher"),
    path("postteacher", views.teacherData.as_view(), name="postteacher"),
    path("putteacher", views.teacherData.as_view(), name="putteacher"),
    path("patchteacher", views.teacherData.as_view(), name="patchteacher"),
    path("deleteteacher", views.teacherData.as_view(), name="deleteteacher"),

]
