#the class where the action happens
import pandas as pd
import numpy as np
import k_means_clustering
from sklearn.preprocessing import Normalizer
from db_interactor import DBInteractor
from preprocess import Preprocessor
from k_means_clustering import kmeans
import sys
if __name__ == '__main__':
    #np.set_printoptions(threshold=np.inf)


    #create a DB interactor
    interactor = DBInteractor("batting")

    #Only get player id's
    get_playerids = interactor.load_data_frame_from_table(table_name="batting", complete_query="SELECT playerID FROM batting WHERE AB>50")
    playerid_matrix = interactor.df_to_numpy_matrix()
    subset_playerid_matrix = playerid_matrix[np.shape(get_playerids)[0] - 4000:np.shape(get_playerids)[0]-1,:]



    #Get player id, year, team
    get_compelteplayerinfo = interactor.load_data_frame_from_table(table_name="batting", complete_query="SELECT playerID,yearID,teamID FROM batting WHERE AB>50")
    playerinfo_matrix = interactor.df_to_numpy_matrix()
    subset_playerinfo_matrix = playerinfo_matrix[np.shape(get_compelteplayerinfo)[0] - 4000:np.shape(get_compelteplayerinfo)[0]-1,:]

    #Get data for players
    get_player_data = interactor.load_data_frame_from_table(table_name="batting", complete_query="SELECT R,H,TWOB,THREEB,H,R,RBI,SB,CS,BB,SO,IBB,HBP,SF,SH,GIDP FROM batting WHERE AB > 50")
    playerdata_matrix = interactor.df_to_numpy_matrix()
    subset_playerdata_matrix = playerdata_matrix[np.shape(get_player_data)[0] - 4000:np.shape(get_player_data)[0]-1, :]

    #All data for players
    get_allplayer_data = interactor.load_data_frame_from_table(table_name="batting",
                                                            complete_query="SELECT playerID, yearID, teamID, G,AB,R,H,TWOB,THREEB,H,R,RBI,SB,CS,BB,SO,IBB,HBP,SF,SH,GIDP FROM batting WHERE AB > 50")
    allplayerdata_matrix = interactor.df_to_numpy_matrix()
    subset_allplayerdata_matrix = allplayerdata_matrix[np.shape(get_allplayer_data)[0] - 4000:np.shape(get_allplayer_data)[0]-1, :]

    interactor.disconnect()

    k = kmeans()

    means = k.initialize_means(subset_playerdata_matrix,400)
    k.print_means()
    #sys.exit()
    final_clusters = k.k_means_algorithm(subset_playerdata_matrix,means)

    for x in range(0, 400):
        for y in range(0, len(final_clusters)):
            if final_clusters[y] == x:
                print(subset_allplayerdata_matrix[y,:])
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
