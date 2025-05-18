from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'pages/index.html', context)
