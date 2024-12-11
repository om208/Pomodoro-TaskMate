from django.shortcuts import render
from django.http import HttpResponse

def AdditionalTestingView(request):
    return HttpResponse("Welcome to the Management App Index Page.")
