from django.urls import path
from .views import web_design

urlpatterns = [
    path('', web_design, name='web_design'),
]