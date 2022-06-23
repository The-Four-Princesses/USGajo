from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'intro_program/home.html')

def intro_pdu(request):
    return render(request, 'intro_program/pdu.html')

def intro_usc(request):
    return render(request, 'intro_program/usc.html')

#def default_map(request):
    #return render(request, 'default.html', {})