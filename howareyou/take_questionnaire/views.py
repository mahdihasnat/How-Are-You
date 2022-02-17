# Create your views here.
from django.shortcuts import render,redirect
from take_questionnaire.models import Question,Test

def render_test(request):
    test = Test.objects.get(name='General')
    questions = Question.objects.filter(test=test)
    questions_text = []
    for question in questions:
        questions_text.append(question.question_text)
    print(questions_text)
    return render(request, 'take_questionnaire/test-questions.html', {'name' : 'Self-Rated Level 1 Cross-Cutting Symptom Measure', 'questions' : questions_text})

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
