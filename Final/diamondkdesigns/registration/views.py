from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UserProfile

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  

# Sign up view
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'  
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Create a UserProfile associated with the new user
        UserProfile.objects.create(user=form.instance)
        return response

# Profile view
def profile(request):
    return render(request, 'profile.html')