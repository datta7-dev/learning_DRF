from django.shortcuts import render, HttpResponse


# default home page
def index(request):
    return HttpResponse("<h1>welcome to django rest framework</h1>")
