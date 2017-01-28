from django.shortcuts import render
from django.http import HttpResponse
from nsetools import Nse
from .models import Greeting
from django.http import JsonResponse

# Create your views here.
def index(request,code=None):
    # return HttpResponse('Hello from Python!')
    nse = Nse()
    if nse.is_valid_code(code):
        print code
        q = nse.get_quote(str(code))
        return JsonResponse(q)

    return HttpResponse("not valide")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


