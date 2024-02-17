from django.shortcuts import render
from .models import ContactMessage

# Create your views here.
def contact(request):
    if request.method == 'POST':
        # Handle form submission if needed
        pass
    return render(request, 'contact.html')