from django.urls import path
from genericViews import views

urlpatterns = [
    path("", views.genericApiViews, name="genericviews"),
    path("listteacher", views.listTeacher.as_view(), name="listteacher"),
    path("createteacher", views.createTeacher.as_view(), name="createteacher"),
    path("retrieveteacher/<int:pk>",
         views.retrieveTeacher.as_view(), name="retrieveteacher"),
    path("updateteacher/<int:pk>",
         views.updateTeacher.as_view(), name="updateteacher"),
    path("destroyteacher/<int:pk>",
         views.destroyTeacher.as_view(), name="destroyteacher"),
]
