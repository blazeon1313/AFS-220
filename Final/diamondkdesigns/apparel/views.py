from django.shortcuts import render
from .models import ApparelDesign

# Create your views here.
def apparel(request):
    apparel_designs = ApparelDesign.objects.all()

    context = {'apparel_designs': apparel_designs}

    return render(request, 'apparel.html', context)