from django.shortcuts import render
from .models import DecalDesign

# Create your views here.
def decal(request):
    decal_designs = DecalDesign.objects.all()

    context = {'decal_designs': decal_designs}


    return render(request, 'decal.html', context)