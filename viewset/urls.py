from django.urls import path, include
from viewset import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("teacherviewset", views.teacherViewset, basename="teacher")

urlpatterns = [
    path("", views.viewSet, name="viewset"),
    path("viewset", include(router.urls)),
]