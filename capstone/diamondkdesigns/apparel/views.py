from django.shortcuts import render

# Create your views here.
def clothing(request):
    return render(request, 'clothing.html')