from django.shortcuts import render

# Create your views here.

def decal(request):
    return render(request, 'decal.html')
