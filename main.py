#the class where the action happens
import pandas as pd
import numpy as np
import sys
import k_means_clustering
from sklearn.preprocessing import Normalizer
from db_interactor import DBInteractor
from preprocess import Preprocessor
from k_means_clustering import kmeans
class Main:
    def get_thing(self):
        return self.thing

    def get_player_row(self, firstname, lastname, year, all_data, player_data, cluster):
        count = 0
        for x in xrange(0, len(player_data)):
            if player_data[x][0] == firstname and player_data[x][1] == lastname and player_data[x][2] == year:
                count = x
                break
        clust_val = cluster[count]
        similar = []
        for y in xrange(0, len(cluster)):
            if cluster[y] == clust_val:
                similar.append(y)
        # print len(similar)
        # print np.shape(all_data)[1]
        arr = []
        for z in xrange(0, len(similar)):

            arr.append(all_data[similar[z], :])
            #sim_athletes[z, :] = all_data[similar[z], :]

        return arr





    def __init__(self, first, last, year):
        #np.set_printoptions(threshold=np.inf)

        #create a DB interactor
        interactor = DBInteractor("batting")

        #Only get player id's
        get_playerids = interactor.load_data_frame_from_table(table_name="season_bat_order", complete_query="SELECT name_first,name_last FROM season_bat_order WHERE AB>50")
        # print get_playerids
        # sys.exit()
        playerid_matrix = interactor.df_to_numpy_matrix()
        subset_playerid_matrix = playerid_matrix[np.shape(get_playerids)[0] - 2000:np.shape(get_playerids)[0]-1,:]



        #Get player id, year, team
        get_compelteplayerinfo = interactor.load_data_frame_from_table(table_name="season_bat_order", complete_query="SELECT name_first,name_last,yearID FROM season_bat_order WHERE AB>50")
        #print get_compelteplayerinfo.values[0][0]
        #sys.exit()
        playerinfo_matrix = interactor.df_to_numpy_matrix()
        subset_playerinfo_matrix = playerinfo_matrix[np.shape(get_compelteplayerinfo)[0] - 2000:np.shape(get_compelteplayerinfo)[0]-1,:]

        #Get data for players
        get_player_data = interactor.load_data_frame_from_table(table_name="season_bat_order", complete_query="SELECT R,H,TWOB,THREEB,HR,RBI,SB,CS,BB,SO,IBB,SF,SH,GIDP FROM season_bat_order WHERE AB > 50")
        playerdata_matrix = interactor.df_to_numpy_matrix()
        subset_playerdata_matrix = playerdata_matrix[np.shape(get_player_data)[0] - 2000:np.shape(get_player_data)[0]-1, :]

        #All data for players
        get_allplayer_data = interactor.load_data_frame_from_table(table_name="season_bat_order",
                                                                complete_query="SELECT name_first,name_last, yearID, G,AB,R,H,TWOB,THREEB,HR,RBI,SB,CS,BB,SO,IBB,SF,SH,GIDP FROM season_bat_order WHERE AB > 50")
        allplayerdata_matrix = interactor.df_to_numpy_matrix()
        subset_allplayerdata_matrix = allplayerdata_matrix[np.shape(get_allplayer_data)[0] - 2000:np.shape(get_allplayer_data)[0]-1, :]

        interactor.disconnect()

        #print(get_player_row("Barry","Zito", 2004, subset_allplayerdata_matrix,subset_playerinfo_matrix, ))

        k = kmeans()

        means = k.initialize_means(subset_playerdata_matrix,200)
        final_clusters = k.k_means_algorithm(subset_playerdata_matrix,means)

        a =  self.get_player_row(first, last, year, subset_allplayerdata_matrix, subset_playerinfo_matrix, final_clusters)
        for item in a:
            print item

        self.thing = a

# a =  get_player_row("Barry", "Zito", 2004, subset_allplayerdata_matrix, subset_playerinfo_matrix, final_clusters)
# for item in a:
#     print item
#
# self.thing = a
        # for x in range(0, 400):
        #     for y in range(0, len(final_clusters)):
        #         if final_clusters[y] == x:
        #             print(subset_allplayerdata_matrix[y,:])
        #     print("")
        #     print("")
        #     print("")
        #     print("")
        #     print("")
        #     print("")
        #     print("")
        #     print("")
        #     print("")
if __name__ == '__main__':
    m = Main("Barry", "Zito", 2004)
    thing = m.get_thing()
    for item in thing:
        print item
