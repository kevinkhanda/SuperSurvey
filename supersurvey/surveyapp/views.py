from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hi, folk! You are on a Super Survey index.")
