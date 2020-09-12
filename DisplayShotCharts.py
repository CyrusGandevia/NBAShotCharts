# Cyrus Gandevia | NBAShotCharts Project

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats
import urllib.request


# Season ID represents the year the season takes place (ex. 2019-20)
# Season Type represents what stage of the season we're looking at (ex. Pre-season, Regular, Playoffs)
def get_player_shot_chart_info (player_name, season_id, season_type):

    # Searching for requested player
    all_nba_players = players.get_players()
    player_dict = [player for player in all_nba_players if player['full_name'] == player_name][0]

    # Creating the dataframe for the player's career
    career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
    career_df = career.get_data_frames()[0]

    # Finding the team that the player played for during the season
    team_id = career_df[career_df['SEASON_ID'] == season_id]['TEAM_ID']

    # Endpoints to acquire the shot chart detail
    shot_chart = shotchartdetail.ShotChartDetail(team_id=int(team_id),
                                                 player_id=int(player_dict['id']),
                                                 season_type_all_star=season_type,
                                                 season_nullable=season_id,
                                                 context_measure_simple="FGA").get_data_frames()

    return shot_chart[0]


def display_basketball_court(axes, court_lines_color = "black", court_lines_width = 2):
    # Creating a NBA Style Half Court to Display Shots from:

    # Hoop
    hoop = Circle((0, 0), radius=7.5, linewidth=court_lines_width, color=court_lines_color, fill=False)

    # 2D Backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=court_lines_width, color=court_lines_color)

    # The Paint
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=court_lines_width, color=court_lines_color, fill=False)
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=court_lines_width, color=court_lines_color, fill=False)

    # Free Throw Arcs
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=court_lines_width, color=court_lines_color, fill=False)
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=court_lines_width, color=court_lines_color,
                            linestyle='dashed')

    # Restricted Area
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=court_lines_width, color=court_lines_color)

    # Three Point Arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=court_lines_width, color=court_lines_color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=court_lines_width, color=court_lines_color)
    three_arc = Arc((0, 3), 474.75, 475, theta1=22, theta2=158, linewidth=court_lines_width, color=court_lines_color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=court_lines_width, color=court_lines_color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=court_lines_width, color=court_lines_color)

    # Outer Lines
    outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=court_lines_width, color=court_lines_color, fill=False)

    # List of all elements to be plotted onto the areas
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc, outer_lines]

    # Add Court Elements onto the Axes
    for element in court_elements:
        axes.add_patch(element)

    return axes


def display_shot_chart (data, title):

    # Create new axes object and plot lines to create the basketball half court where data is displayed
    axes = plt.gca()
    display_basketball_court(axes)

    # Set axes boundaries and hide labels
    axes.set_xlim(-250, 250)
    axes.set_ylim(422.5, -47.5)
    axes.axes.get_xaxis().set_visible(False)
    axes.axes.get_yaxis().set_visible(False)

    # Grouping data based off made and missed shots
    x_missed = data[data['EVENT_TYPE'] == 'Missed Shot']['LOC_X']
    y_missed = data[data['EVENT_TYPE'] == 'Missed Shot']['LOC_Y']
    x_made = data[data['EVENT_TYPE'] == 'Made Shot']['LOC_X']
    y_made = data[data['EVENT_TYPE'] == 'Made Shot']['LOC_Y']

    made_shots_amount = x_made.count()
    missed_shots_amount = x_missed.count()
    total_shots_taken = made_shots_amount + missed_shots_amount
    fg_percentage = round ((made_shots_amount/total_shots_taken) * 100, 1)

    # Title of chart, citing sources for data
    axes.set_title(title, fontsize=18)
    axes.text(-250, 480, 'Data Source: stats.nba.com\nAuthor: Cyrus Gandevia', fontsize=10)

    # FG Percentage Statistic
    axes.text(-250, 445, 'FG %: ', fontsize=12)
    axes.text(-216, 447.5, str(fg_percentage) + '%', fontsize=22, weight='heavy')
    axes.text(-160, 445, "(" + str(made_shots_amount) + "-" + str(total_shots_taken) + ")", fontsize=12)

    # Plotting missed shots (with a Red X-mark)
    axes.scatter(x_missed, y_missed, c='r', marker="x", label="Missed Shot", s=100, linewidths=2.5)

    # Plotting made shots (with a Green Circle)
    axes.scatter(x_made, y_made, facecolors='none', edgecolors='g', marker='o', label="Made Shot", s=100, linewidths=2.5)

    # Legend for Chart
    axes.legend()


if __name__ == "__main__":
    nba_player = "Kobe Bryant"  # ex. "Stephen Curry"
    season_year = "2015-16"  # ex. 2015-16
    season_type = "Regular Season"  # Choose between "Preseason" "Regular Season", "Playoffs"

    title = nba_player + " FGA\n" + season_year + " " + season_type

    player_shot_chart_df= get_player_shot_chart_info(nba_player, season_year, season_type)
    plt.figure(figsize=(12, 11))
    plt.rcParams["font.family"] = "Ayuthaya"
    display_shot_chart(player_shot_chart_df, title=title)
    plt.xlim(-250, 250)
    plt.ylim(422.5, -47.5)
    plt.show()