from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user profile if needed
    # For example:
    # bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    class Meta:
        app_label = 'registration'
        
    def __str__(self):
        return self.user.username