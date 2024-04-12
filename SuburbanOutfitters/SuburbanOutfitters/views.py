from django.shortcuts import render

def home(request):
    context = {
        'slides': range(1, 4) 
    }
    return render(request, 'home.html', context)
