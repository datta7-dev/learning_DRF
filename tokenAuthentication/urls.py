from django.urls import path
from tokenAuthentication import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.tokenAuthHome, name="tokenauthhome"),
    path("gettoken", obtain_auth_token),
]
