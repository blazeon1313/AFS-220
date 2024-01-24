from django.shortcuts import render
from .models import WebProject

# Create your views here.
def web_design(request):
    web_projects = WebProject.objects.all()
    return render(request, 'web_design.html', {'web_projects': web_projects})