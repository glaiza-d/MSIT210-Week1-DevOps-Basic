from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'home',
        'course': 'MSIT217 - WebAppDev',
        'units': 3,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'about'})