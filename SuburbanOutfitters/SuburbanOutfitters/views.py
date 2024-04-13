from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'slides': range(1, 4) 
    }
    return render(request, 'home.html', context)
