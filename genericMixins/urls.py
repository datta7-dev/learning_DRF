from django.urls import path
from genericMixins import views
urlpatterns = [
    path("", views.genericMixins, name="genericmixins"),
    path("listteacher", views.listTeacher.as_view(), name="listteacher"),
    path("createteacher", views.createTeacher.as_view(), name="createteacher"),
    path("updateteacher/<int:pk>",
         views.updateTeacher.as_view(), name="updateteacher"),
    path("getteacher/<int:pk>",
         views.getTeacher.as_view(), name="getteacher"),
    path("deleteteacher/<int:pk>",
         views.destroyTeacher.as_view(), name="deleteteacher"),
]
