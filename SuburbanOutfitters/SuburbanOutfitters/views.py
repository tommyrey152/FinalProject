from django.shortcuts import render




def home(request):
  return render(request, 'home.html', {})

def home(request):
    context = {
        'slides': range(1, 4)  # Assumes you have 3 slides, adjust as necessary
    }
    return render(request, 'home.html', context)