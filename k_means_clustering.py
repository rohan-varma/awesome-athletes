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
            means_matrix[x:,] = data_matrix[rand_numbers[rand_index], :].reshape(np.shape(data_matrix)[1])
            rand_numbers = rand_numbers[:rand_index] + rand_numbers[rand_index + 1:]

        return means_matrix

    def k_means_algorithm(self, data, means):

        previous_cluster_num = [0] * np.shape(data)[0]

        cluster_num = [0] * np.shape(data)[0]

        while(True):

            for i in range(0, np.shape(data)[0]):

                sum_of_squares_list = [0] * np.shape(means)[0]

                for j in range(0, np.shape(means)[0]):

                    sum = 0

                    for k in range(0, np.shape(means)[1]):

                        sum = sum + (data[i, k] - means[j, k]) * (data[i, k] - means[j, k])

                    sum_of_squares_list.insert(j, math.sqrt(sum))
                    sum_of_squares_list.pop(j + 1)

                cluster_num.insert(i,sum_of_squares_list.index(min(sum_of_squares_list)))
                cluster_num.pop(i+1)

            print(cluster_num)
            if (self.comparelists(cluster_num, previous_cluster_num)):

                return cluster_num

                break

            else:

                previous_cluster_num = cluster_num

                for l in range(0, np.shape(means)[0]):

                    rows_in_which_clusters = np.zeros((1, np.shape(data)[1]))
                    num_points_in_cluster = 0

                    for m in range(0, len(cluster_num)):

                        if cluster_num[m]==l:

                            rows_in_which_clusters += data[m, :]
                            num_points_in_cluster = num_points_in_cluster + 1

                    rows_in_which_clusters = rows_in_which_clusters/num_points_in_cluster
                    means[l, :] = rows_in_which_clusters[0, :]

    def comparelists(self, list1, list2):

        for i in range(0, len(list1)):

            if list1[i] == list2[i]:

                continue
            else:

                return False

        return True

if __name__ == '__main__':
    k=kmeans()
    matrix = np.random.randint(5, size=(30, 20))
    print(matrix)
    means= k.initialize_means(matrix, 4)
    final = k.k_means_algorithm(matrix,means)
    print(final)