from django.db import models
import datetime
# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    GAME_TYPE_CHOICES = [
        ('HOME', 'Home'),
        ('AWAY', 'Away'),
    ]
    game_date = models.DateField(null=True, blank=True)
    game_time = models.TimeField(default=datetime.time(12, 0, 0), null=True, blank=True)
    opponent = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    game_type = models.CharField(
        max_length=4,  # Max length for 'HOME' or 'AWAY'
        choices=GAME_TYPE_CHOICES,
        default='HOME'  # Default to 'HOME' game type
    )
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='schedules', null=True)


    def __str__(self):
        """
        Returns a human-readable string representation of the Schedule,
        explicitly stating home and away teams.
        """
        date_str = self.game_date.strftime('%Y-%m-%d') if self.game_date else "N/A Date"
        time_str = self.game_time.strftime('%I:%M %p') if self.game_time else "N/A Time" # e.g., 03:00 PM
        league_name_str = self.league.name if self.league else "N/A League"

        my_team_name = "Clique Mambas" # Your team's fixed name

        if self.game_type == 'HOME':
            home_team_display = my_team_name
            away_team_display = self.opponent
        else: # self.game_type == 'AWAY'
            home_team_display = self.opponent
            away_team_display = my_team_name

        return (
            f"{home_team_display} (Home) vs {away_team_display} (Away) on "
            f"{date_str} at {time_str} in {league_name_str} at {self.location}"
        )
        
    class Meta:
        ordering = ['game_date', 'game_time']