from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100, default='New Player')
    height_ft= models.DecimalField(max_digits=3, decimal_places=1, max_length=5, blank=True, null=
    True)  # height in feet
    position = models.CharField(max_length=50, blank=True, null=True, choices=[
        ('Point Guard', 'Point Guard'),
        ('Shooting Guard', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center'),
    ])
    jersey_number = models.PositiveIntegerField(unique=True)
    image = CloudinaryField('Player Photo', blank=True, null=True)
    weight_kgs = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # weight in kgs
    def __str__(self):
        return f"{self.name} - #{self.jersey_number} ({self.position})"

    class Meta:
        verbose_name_plural = 'Players'
        ordering = ['jersey_number']
