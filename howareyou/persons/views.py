from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'persons/home.html')
    # return HttpResponse('Hello, world. You are at the persons index.')
