# NBAShotCharts

What does it do?
------------

I've created a script that extracts data from the NBA Stats API and creates a neat visualization of a basketball player's field goal attempts over a specific season. The visualization of this data is called a "shot chart."

Why did I create it?
------------

The NBA Stats page makes it very inaccessible to find a player's shot chart data. It gets even more difficult when you try to apply filters for which season you are looking for, as well as for the type of setting the shots took place in (eg. playoffs or regular season). I decided to make a script of my own that would allow me to easily see this data for numerous players, without much of a hassle. 

Functionality
------------

The script allows the user to select the following parameters:
  - The <b>NBA Player</b> that you would like to see the field goal attempts for (e.g. Stephen Curry)
  - The <b>Season Date</b> for which the NBA Player played in (e.g. 2015-16)
  - The <b>Type of Season</b> for which the NBA Player's shots are being tracked for (e.g. "Preseason", "Regular Season" or "Playoffs")
  
The script supports both <b>currently active</b> as well as <b>inactive</b> NBA Players. However it should be noted that the NBA Stats only goes as far back as the 1996-97 season in terms of shot tracking data. Unfortunately we can't see Michael Jordan's 1995-96 season :(

This script utilizes matplotlib, pandas, and the requests library to bring it all together.

Shot Chart Visualizations of Historical NBA Moments
------------

<b> Stephen Curry's Unanimous MVP Season (2015-16): </b>

<div class="row">
<img src="https://i.imgur.com/MomWJ4B.png" height="750" width="756">
<img src="https://i.imgur.com/kNQe74V.png" height="750" width="756">
</div>
<br>

<b> LeBron James' Insane 56.7% FG Season (2013-14): </b>

<div class="row">
<img src="https://i.imgur.com/a9NsBvW.png" height="750" width="756">
<img src="https://i.imgur.com/vWkR56l.png" height="750" width="756">
</div>

<br>

<b> Michael Jordan's Second Three-Peat Season (1997-98): </b>
<div class="row">
<img src="https://i.imgur.com/860wOKC.png" height="750" width="756">
<img src="https://i.imgur.com/9l341v2.png" height="750" width="756">
</div>


Want to try it out yourself?
------------

### Requirements: 
- Python 2.7 or 3.3+

- [matplotlib](http://matplotlib.sourceforge.net)
- [pandas](http://pandas.pydata.org/)
- [requests](http://docs.python-requests.org/en/latest/)

Once you meet the following requirements, just download the script and in the "__main__" function, input what you'd like for the following variables:
- nba_player
- season_year
- season_type

TODO
------------
I would eventually like to find a way to add a player's headshot in these shot charts, to help better put a name to the face when you're looking at these charts. The current challenge is that accessing many of the player's current and past year headshots are restricted on sites such as NBA.com and ESPN.com

Credits
------------
Big shoutout to Savvas Tjortjoglou for inspiration on how to draw the court-shaped plot!
