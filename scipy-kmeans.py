import pandas as pd
import numpy as np
import k_means_clustering
from sklearn.preprocessing import Normalizer
from db_interactor import DBInteractor
from preprocess import Preprocessor

from sklearn import mixture, metrics
from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.datasets import make_blobs
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
#import matplotlib.pyplot as plt

#fig = plt.figure(figsize=(10,10),  dpi = 1000)
def fit_samples_gmm(samples, n_components):
    gmix = mixture.GMM(n_components=n_components, covariance_type='diag')
    gmix.fit(samples)
#     print gmix.means_
#     print gmix.predict(samples)
    colors = ['r' if i==0 else 'g' for i in gmix.predict(samples)]
    # ax = plt.gca()
    # ax.scatter(samples[:,0], samples[:,1], alpha=0.8)
    # plt.show()

def fit_samples_kmeans(samples, n_features, n_clusters):
    n_samples = len(samples)/4
    random_state = 150
    X, y = make_blobs(n_samples=300, n_features=n_features, centers=n_clusters, random_state=random_state)
    y_pred = KMeans(n_clusters=n_clusters, random_state=random_state).fit_predict(X)
    print X[:, 0]
    print X[:, 1]
    # plt.subplot(111)
    # plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    print len(y_pred)
    #plt.show()

def fit_affinity_propagation(samples):
    n_samples = len(samples)/10
    random_state = 0
    X, labels_true = make_blobs(n_samples=n_samples, cluster_std=0.5,
                               random_state=random_state)
    af = AffinityPropagation(preference=-50).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)

    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f"
          % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f"
          % metrics.adjusted_mutual_info_score(labels_true, labels))
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(X, labels, metric='sqeuclidean'))

    ##############################################################################
    # Plot result
    # plt.close('all')
    # plt.figure(1)
    # plt.clf()
    #
    # colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    # for k, col in zip(range(n_clusters_), colors):
    #     class_members = labels == k
    #     cluster_center = X[cluster_centers_indices[k]]
    #     plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    #     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
    #              markeredgecolor='k', markersize=14)
    #     for x in X[class_members]:
    #         plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
    #
    # plt.title('Estimated number of clusters: %d' % n_clusters_)
    # plt.show()
    return af

if __name__ == '__main__':

    np.set_printoptions(threshold=np.inf)
    #create a DB interactor
    interactor = DBInteractor("season_batting")
    #gets the dataframe
    df = interactor.get_current_data_frame()
    #print(df)
    #df = df.drop(['yearID','stint','stint','teamID','lgId','HBP', 'playerID'], axis=1)
    arr_with_ids = interactor.df_to_numpy_matrix()
    cols = ['playerID', 'yearID']
    df = interactor.drop_useless_stuff(cols)
    #converts it to a numpy matrix
    arr = interactor.df_to_numpy_matrix()
    arr = arr.astype(float)
    #print arr
    #print arr
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    #this doesn't do anything very useful right now

    p = Preprocessor(arr, df)
    arr = p.preprocess(arr)
    sample = arr
    print arr.shape[1]
    fit_samples_gmm(sample,1)
    fit_samples_kmeans(sample, sample.shape[1], 10)
    rand_indices = np.random.choice(np.arange(0,len(sample)), replace=False, size=len(sample))
    rand_samples = sample[rand_indices]
    af = fit_affinity_propagation(samples=rand_samples)
