
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Person
from patients.models import Patient
from psychiatrists.models import Psychiatrist

# Create your views here.

def index(request):
    return render(request, 'persons/home.html')
    # return HttpResponse('Hello, world. You are at the persons index.')

# def patient_home(request):
#     return render(request, 'patients/patient-home.html')

def login(request):
    if request.method == 'POST':
        try:
            user = Patient.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
            request.session['username'] = user.username
            return redirect('patients:patient_home')
        except Patient.DoesNotExist:
            print("Patient not found")
            try:
                user = Psychiatrist.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
                print("Psychiatrist logged in")
                return redirect(request, 'psychiatrists/psyc.html',{"name":user.username})
            except Psychiatrist.DoesNotExist:
                print("Psychiatrist not found")
                return redirect(request, 'persons/home.html',)
    else:
        return redirect('/')