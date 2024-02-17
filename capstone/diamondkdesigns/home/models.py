from django.db import models

# Create your models here.
class FeaturedItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured_items', default='featured_items/DiamondK.jpg')

    def __str__(self):
        return self.title