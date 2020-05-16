from nba_api.stats.endpoints import playercareerstats
import json
import os

# Messing around with API Features
career_stats = playercareerstats.PlayerCareerStats(player_id=2544)
ID = career_stats.career_totals_regular_season.get_dict()
#print(ID)