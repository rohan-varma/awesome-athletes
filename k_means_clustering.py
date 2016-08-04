#This class implements the k-means algorithm to cluster the data.
import random
import numpy as np
import math



class kmeans:
    def __init__(self):
        pass

    def initialize_means(self, data_matrix, num_clusters):

        means_matrix = np.zeros((num_clusters,np.shape(data_matrix)[1]))

        rand_numbers = list(range(0,np.shape(data_matrix)[0]))

        for x in range(0, np.shape(means_matrix)[0]):

            rand_index = random.randint(0, (len(rand_numbers)-1))
            rand_vec = data_matrix[rand_numbers[rand_index], :].reshape(np.shape(data_matrix)[1])
            rand_numbers = rand_numbers[:rand_index] + rand_numbers[rand_index+1 :]
            means_matrix[x:,] = rand_vec

        return means_matrix

    def k_means_algorithm(self, data, means):

        previous_cluster_num = []

        print(means)

        while(True):

            cluster_num = []

            for i in range(0, np.shape(data)[0]):

                sum_of_squares_list = []

                for j in range(0, np.shape(means)[0]):

                    sum = 0

                    for k in range(0, np.shape(means)[1]):

                        sum = sum + (data[i, k] - means[j, k]) * (data[i, k] - means[j, k])

                    sum_of_squares_list.append(math.sqrt(sum))


                cluster_num.append(sum_of_squares_list.index(min(sum_of_squares_list)))

            if (cmp(cluster_num, previous_cluster_num)):

                return cluster_num

                break

            else:
                previous_cluster_num = cluster_num

                var = 0

                while var < np.shape(means)[0]:

                    common_cluster_data_points = np.zeros((1, np.shape(data)[1]))
                    num_points_in_cluster = 0

                    for l in range(0, len(cluster_num)):

                        if cluster_num[l]==var:
                            common_cluster_data_points += data[l, :]
                            num_points_in_cluster = num_points_in_cluster + 1

                    common_cluster_data_points = common_cluster_data_points/num_points_in_cluster

                    means[var, :] = common_cluster_data_points[1, :]














if __name__ == '__main__':
    k=kmeans()
    matrix = np.matrix('1 2; 3 4; 5 6; 7 8; 9 10; 11 12; 13 14; 15 16; 17 18; 19 20')
    print(matrix)
    means= k.initialize_means(matrix, 2)
    print(k.k_means_algorithm(matrix,means))
