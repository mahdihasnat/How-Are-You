from django.http import HttpResponse


# Create your views here.

def take_questionnaire(request):
    response = HttpResponse("Now please render")
    return response
    # return render(request, "hello")
