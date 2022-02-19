# Create your views here.
from doctest import testfile
from django.shortcuts import render,redirect,HttpResponseRedirect
from take_questionnaire.models import Question,Test,TestResult,Answer,Rule
from patients.models import Patient

def render_test(request):
    
    context = {}
    test = Test.objects.get(name='General')
    context['test'] = test
    context['my'] = Patient.objects.get(username=request.session['username'])
    return render(request, 'take_questionnaire/test-questions.html',context)

def get_score(question,option):
    rule = Rule.objects.get(question_id=question,option_id=option)
    return rule.rubric_score

def submit(request,test_id):
    if request.method == 'POST':
        print(request.POST)
        test = Test.objects.get(id=test_id)
        patient = Patient.objects.get(username=request.session['username'])
        test_result = TestResult.objects.create(patient=patient,test=test)
        for question in test.questions.all():
            try:
                response = request.POST[str(question.id)]
            except:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        for question in test.questions.all():
            response = request.POST[str(question.id)]
            answer = Answer.objects.create(testresult=test_result,question=question,response=response)
            answer.score = get_score(question,response)
            answer.save()
        print("Inside response-recorded")
        return render(request, 'take_questionnaire/response-recorded.html')
    else:
        return redirect('take_questionnaire:render_test')
    
    




# This is actually user homepage :3
# def render_test_list(request):
#
#     return HttpResponse('return all  tests!')


# def render_submitted(request):
#     return render(request, 'take_questionnaire/response-recorded.html')
