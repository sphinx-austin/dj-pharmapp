from django.shortcuts import render


# third party imports
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

