from nba_api.stats.endpoints import playercareerstats, PlayerDashboardByGameSplits, playerdashboardbyyearoveryear, playerdashboardbylastngames, PlayerGameLog
import nba_api.stats.endpoints as nba

career = playercareerstats.PlayerCareerStats(player_id='203076')
ad = career.get_data_frames()[0]

import pandas as pd

type(ad)
ad.columns
ad.FG3_PCT.mean()
ad.FT_PCT.mean()

ad_games = PlayerDashboardByGameSplits(player_id='203076', date_from_nullable= '10-20-2016')

ad_log = ad_games.get_data_frames()[0]
ad_log

ad_time = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id='203076')
ad_time.get_data_frames()[0]

ad_last_20 = playerdashboardbylastngames.PlayerDashboardByLastNGames(player_id='203076', last_n_games=20)

ad_last_20.get_data_frames()[0]
ad_2016_game_log = PlayerGameLog(player_id='203076', season=2016).get_data_frames()[0]

ad_2016_game_log.head()

nba.BoxScoreDefensive(game_id='0021900475').get_data_frames()[0].columns


  
