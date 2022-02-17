# Create your views here.
from django.shortcuts import render


def render_a_test(request):
    # test = ["OCD", "HISTERIA"]
    # dict = {"test" : test}
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'take_questionnaire/test-questions.html')


# This is actually user homepage :3
# def render_test_list(request):
#
#     return HttpResponse('return all  tests!')


def render_submitted(request):
    return render(request, 'take_questionnaire/response-recorded.html')
