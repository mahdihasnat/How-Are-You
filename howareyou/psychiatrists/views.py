from django.shortcuts import redirect, render

from django.utils import timezone
from .models import Psychiatrist
from take_questionnaire.models import Answer, TestResult,Dieases
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
	context['dieaseses'] = Dieases.objects.all()
	context['psychiatrists'] = Psychiatrist.objects.all()
	return render(request, 'psychiatrists/test_result_varify.html',context)

def test_result_save(request,test_result_id):
	if request.method == 'POST':
		testresult = TestResult.objects.get(id=test_result_id)
		for psychiatrist in Psychiatrist.objects.all():
			if psychiatrist.username in request.POST:
				testresult.consultations.add(psychiatrist)
		testresult.verifier = Psychiatrist.objects.get(username=request.session['username'])
		testresult.verification_time=timezone.now()
		print(request.POST)
		for dieases in Dieases.objects.all():
			if str(dieases.id) in request.POST:
				testresult.dieaseses.add(dieases)
		testresult.save()
		return redirect('psychiatrists:test_result_poll')
	else:
		return redirect('psychiatrists:test_result_poll')