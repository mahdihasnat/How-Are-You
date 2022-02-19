from django.shortcuts import render

from .models import Psychiatrist
# Create your views here.

def psychiatrist_home(request):
	assert('username' in request.session)
	context={}
	context['my'] = Psychiatrist.objects.get(username=request.session['username'])
	return render(request, 'psychiatrists/psychiatrist_home.html',context)

def test_result_poll(request):
	assert('username' in request.session)
	
	return render(request , 'psychiatrists/test_result_poll.html')