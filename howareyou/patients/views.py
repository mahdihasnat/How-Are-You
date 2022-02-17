from django.shortcuts import render

from .models import Patient
# Create your views here.

def patient_home(request):
	assert('username' in request.session)
	context={}
	context['my']=Patient.objects.get(username=request.session['username'])
	return render(request, 'patients/patient-home.html',context)