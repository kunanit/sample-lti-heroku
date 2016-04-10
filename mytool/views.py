from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
	return HttpResponse("hello world")

@csrf_exempt
def lti_launch(request):
	return HttpResponse("hello this is the lti tool")