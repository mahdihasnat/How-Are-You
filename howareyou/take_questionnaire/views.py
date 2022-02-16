from django.http import HttpResponse


# Create your views here.

def take_questionnaire(request):
    response = HttpResponse("Here's the text of the web page.")
    return response
    # return render(request, "hello")
