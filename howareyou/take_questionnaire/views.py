# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect

from patients.models import Patient
from take_questionnaire.models import Test, TestResult, Answer, Rule


def render_test(request):
    context = {}
    ''' should be changed to capture the right test'''
    test = Test.objects.get(id=1)
    context['test'] = test
    context['my'] = Patient.objects.get(username=request.session['username'])
    return render(request, 'take_questionnaire/test-questions.html', context)

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
                test_result.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        for question in test.questions.all():
            response = int(request.POST[str(question.id)])
            answer = Answer.objects.create(testresult=test_result,question=question,response=response)
            answer.score = get_score(question,response)
            answer.save()
        # print("Inside response-recorded")
        context = {}
        context ['my'] = Patient.objects.get(username=request.session['username'])
        return render(request, 'take_questionnaire/response-recorded.html',context)
    else:
        return redirect('take_questionnaire:render_test')
    
    




# This is actually user homepage :3
# def render_test_list(request):
#
#     return HttpResponse('return all  tests!')


# def render_submitted(request):
#     return render(request, 'take_questionnaire/response-recorded.html')
