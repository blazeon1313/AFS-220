from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UserProfile

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'  
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response

    def profile(request):
        return render(request, 'profile.html')