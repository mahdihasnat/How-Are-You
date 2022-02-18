# Create your views here.
from django.shortcuts import render,redirect
from take_questionnaire.models import Question,Test

def render_test(request):
    
    context = {}
    test = Test.objects.get(name='General')
    context['test'] = test
    context['questions'] = Question.objects.filter(test=test)
    print(context)
    print(test.questions.all())
    return render(request, 'take_questionnaire/test-questions.html',context)

def render_submit(request):
    #To DO --------------------------------------------
    #Write Response to DB
    #access using request.POST.get()

    
    return render(request, 'take_questionnaire/response-recorded.html')




# This is actually user homepage :3
# def render_test_list(request):
#
#     return HttpResponse('return all  tests!')


# def render_submitted(request):
#     return render(request, 'take_questionnaire/response-recorded.html')
