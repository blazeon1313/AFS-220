from django.shortcuts import render
from .models import FeaturedItem

def home(request):
    featured_items = FeaturedItem.objects.all()

    context = {'featured_items': featured_items}

    return render(request, 'home.html', context)