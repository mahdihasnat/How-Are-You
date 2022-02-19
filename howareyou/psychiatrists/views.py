from django.shortcuts import render

from .models import Psychiatrist
from take_questionnaire.models import Answer, TestResult
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
	testresult = context['testresult'] = TestResult.objects.get(id=test_result_id)
	context['answers'] = [Answer.objects.get(testresult=testresult, question=question) for question in testresult.questions.all()]
	
	return render(request, 'psychiatrists/test_result_varify.html',context)