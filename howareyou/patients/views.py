from multiprocessing import context
from django.shortcuts import render
from take_questionnaire.models import TestResult,Answer
from .models import Patient
# Create your views here.

def patient_home(request):
	assert('username' in request.session)
	context={}
	context['my']=Patient.objects.get(username=request.session['username'])
	return render(request, 'patients/patient-home.html',context)

def verified_reports(request):
	context={}
	patient = context['my']=Patient.objects.get(username=request.session['username'])
	context ['testresults'] = TestResult.objects.filter(patient=patient).exclude(verifier=None)
	return render(request, 'patients/verified-reports.html',context)


def report(request, testresult_id):
	context={}
	testresult=context['testresult'] = TestResult.objects.get(id=testresult_id)
	context['my'] = Patient.objects.get(username=request.session['username'])
	context['answers'] = [Answer.objects.get(testresult=testresult, question=question) for question in testresult.questions.all()]
	return render(request, 'patients/report.html',context)