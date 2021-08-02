from django.urls import path
from jwtAuthentication import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


# api url to get token: http POST http://127.0.0.1:8000/jwtauthentication/gettoken/ username="" password=""
# api url to verify token http POST http://127.0.0.1:8000/jwtauthentication/verifytoken/ token="access_token here"
# api url to refresh token http POST http://127.0.0.1:8000/jwtauthentication/refreshtoken/ refresh="refresh_token here"


""" by default acees token validity is upto 5 minutes
    and refresh token validity is upto 1 day.
"""
urlpatterns = [
    path("", views.jwtHome, name="jwthome"),
    path("gettoken/", TokenObtainPairView.as_view(), name="gettoken"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="refreshtoken"),
    path("verifytoken/", TokenVerifyView.as_view(), name="verifytoken"),
    path("teacherdata", views.teacherData.as_view(), name="teacherdata"),
]
