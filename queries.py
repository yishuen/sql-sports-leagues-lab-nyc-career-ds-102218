def select_name_of_player_with_shortest_name():
    return """SELECT name, length(name) FROM players
    ORDER BY length(name) LIMIT 1; """

def select_all_new_york_players_names():
    return """SELECT players.name FROM players
    JOIN teams ON teams.id = players.team_id
    WHERE teams.name = 'New York Knicks' OR teams.name = 'New York Rangers'; """

def select_team_name_and_total_goals_scored_for_new_york_rangers():
    return """SELECT teams.name, sum(score) FROM teams
    JOIN team_games ON team_games.team_id = teams.id
    WHERE teams.name = 'New York Rangers'; """

def select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl():
    return """SELECT games.date, games.info, teams.name, team_games.score
    FROM games
    JOIN team_games, teams, leagues
    ON teams.id = team_games.team_id AND games.id = team_games.game_id AND leagues.id = teams.league_id
    WHERE leagues.name = 'NHL'; """

def select_date_info_and_total_points_for_highest_scoring_nba_game():
    return """SELECT games.date, games.info, sum(team_games.score) FROM team_games
    JOIN games, teams, leagues
    ON team_games.team_id = teams.id
    AND games.id = team_games.game_id
    AND leagues.id = teams.league_id
    WHERE leagues.name = 'NBA'
    GROUP BY games.date
    ORDER BY sum(score) DESC LIMIT 1;"""
