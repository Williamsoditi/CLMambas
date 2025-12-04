from django.db import models

# Create your models here.
class Schedule(models.Model):
    game_date = models.DateTimeField()
    opponent = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    home_game = models.BooleanField(default=True)

    def __str__(self):
        return f"Clique Mambas Vs {self.opponent} on {self.game_date.strftime('%Y-%m-%d %H:%M')} at ({self.location})"
