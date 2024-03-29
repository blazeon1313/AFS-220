from django.db import models

# Create your models here.
class DecalDesign(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='decal_designs', default='decal_designs/DiamondK.jpg')

    def __str__(self):
        return self.title