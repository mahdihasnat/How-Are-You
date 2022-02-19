from django.shortcuts import render
from pymacaroons import Verifier

from .models import Psychiatrist
from take_questionnaire.models import TestResult
# Create your views here.

def psychiatrist_home(request):
	assert('username' in request.session)
	context={}
	context['my'] = Psychiatrist.objects.get(username=request.session['username'])
	return render(request, 'psychiatrists/psychiatrist_home.html',context)

def test_result_poll(request):
	assert('username' in request.session)
	context={}
	context['my'] = Psychiatrist.objects.get(username=request.session['username'])
	context['testresults'] = TestResult.objects.filter(verifier = None)
	return render(request , 'psychiatrists/test_result_poll.html',context)

def test_result_varify(request,test_result_id):
	context={}
	context['my'] = Psychiatrist.objects.get(username=request.session['username'])
	context['testresult'] = TestResult.objects.get(id=test_result_id)
	return render(request, 'psychiatrists/test_result_varify.html',context)