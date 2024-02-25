from django.urls import path
from .views import contact, thank_you

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('thank-you/', thank_you, name='thank-you'),
]