from django.shortcuts import render
from .models import FeaturedItem

# Create your views here.
def home(request):
    featured_items = FeaturedItem.objects.all()
    return render(request, 'home/home.html', {'featured_items': featured_items})