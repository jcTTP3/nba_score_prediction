import nba_api.stats.endpoints as nba
import nba_api as static
import config
import pandas as pd
import mysql_helper


# Define function to return game logs for the past three seasons
# Will use game ids to feed the boxscore functions

def get_game_logs(year):
    next_ = str(int(year)+1)[-2]
    df = nba.LeagueGameLog(timeout=60, season=year + '-' + next_).get_data_frames()[0]
    return df

seasons = ['2017', '2018', '2019']
dfs = []
for season in seasons:
    dfs.append(get_game_logs(season))
total_logs = pd.concat(dfs)


total_logs['pk'] = total_logs['GAME_ID']+total_logs['TEAM_ABBREVIATION']

# Connect to database
flatiron = mysql_helper.Connection(config.host, config.user, config.password)
nba_db = mysql_helper.DataBase(flatiron, 'nba')

nba_db.insert_fromDf_iteration(total_logs, 'game_logs')
