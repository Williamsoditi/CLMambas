# results_app/models.py
from django.db import models
from schedule.models import Schedule 

class GameResult(models.Model):
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, related_name='result')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    # Example choices for game status
    GAME_STATUS_CHOICES = [
        ('WIN', 'Win'),
        ('LOSS', 'Loss'),
        ('FORFEIT', 'Forfeit'),
    ]
    status = models.CharField(
        max_length=10,
        choices=GAME_STATUS_CHOICES,
        default='UPCOMING'
    )

    # Optional: Add fields for more detailed results
    # quarter_scores = models.JSONField(null=True, blank=True) # e.g., {"q1_home": 25, "q1_away": 20, ...}
    # mvp = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True) # If you have a Player model

    recorded_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        schedule = self.schedule

        date_str = schedule.game_date.strftime('%Y-%m-%d') if schedule.game_date else "N/A Date"
        time_str = schedule.game_time.strftime('%I:%M %p') if schedule.game_time else "N/A Time"

        my_team_name = "Clique Mambas"
        opponent_name = schedule.opponent

        # This logic determines which team is displayed as home and which as away
        if schedule.game_type == 'HOME':
            display_home_team = my_team_name
            display_away_team = opponent_name
        else: # game_type == 'AWAY'
            display_home_team = opponent_name
            display_away_team = my_team_name

        league_name = schedule.league.name if schedule.league else "Unknown League"

        return (
            f"( {self.status} ) ~ {display_home_team} {self.home_score} - "
            f" {display_away_team} {self.away_score} in {league_name} at {schedule.location} - {date_str} {time_str}"
    )

    class Meta:
        verbose_name = "Game Result"
        verbose_name_plural = "Game Results"
        ordering = ['-schedule__game_date', '-recorded_at'] 