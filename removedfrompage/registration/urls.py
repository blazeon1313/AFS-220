from django.urls import path
from .views import CustomLoginView, SignUpView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registration/', SignUpView.as_view(), name='registration'),
]