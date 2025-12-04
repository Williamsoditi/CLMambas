from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100, default='New Player')
    height= models.DecimalField(max_digits=1, decimal_places=1, max_length=5, blank=True, null=
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

    def __str__(self):
        return f"{self.first_name} {self.last_name} - #{self.number} ({self.position})"

    class Meta:
        verbose_name_plural = 'Players'
        ordering = ['jersey_number']
