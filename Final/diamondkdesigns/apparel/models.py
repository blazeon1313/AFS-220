from django.db import models

# Create your models here.
class ApparelDesign(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='apparel_designs', default='apparel_designs/DiamondK.jpg')

    def __str__(self):
        return self.title