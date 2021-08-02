from django.urls import path, include
from modelviewset import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register views class as views.classname
router.register("modelviewset", views.readOnlyTeacherModelViewset,
                basename="modelviewset")

urlpatterns = [
    path("", views.modelViewset, name="modelviewset"),
    # include router urls which we have created above
    path("modelviewset", include(router.urls)),
]
