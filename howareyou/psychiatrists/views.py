from django.shortcuts import render

from .models import Psychiatrist
# Create your views here.

def psychiatrist_home(request):
	assert('username' in request.session)
	context={}
	context['my'] = Psychiatrist.objects.get(username=request.session['username'])
	return render(request, 'psychiatrists/psychiatrist_home.html',context)