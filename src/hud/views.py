from django.shortcuts import render

# Create your views here.

def hud_index(request):
    return render(request, 'hud/index.html')

def hud_pos(request):
    return render(request, 'hud/pos/home.html')