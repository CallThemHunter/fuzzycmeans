#! /usr/bin/env python3
from typing import List
import numpy as np
from numpy.typing import NDArray


class FuzzyCluster:
    def __init__(self, data: NDArray, membership: NDArray, m=2):
        self._m = m
        self.data = data
        self.membership = np.concatenate(
            np.ones((1, membership)),
            np.zeros((1, len(self.data)-membership)))

    def __str__(self):
        out = ""
        out += "\nmembership: " + self.membership.__str__()
        out += "\ndata: " + self.data.__str__()
        out += "\ncentroid: " + self.centroid().__str__()
        return out

    def __len__(self):
        return self.data.__len__()

    def centroid(self):
        partials = np.multiply(self.data, self.membership, axis=0)
        return np.sum(partials)/np.sum(self.membership)


class FuzzyClustering:
    def __init__(self, data: NDArray, k=4):
        self._k = k
        np.random.shuffle(data)
        self.data = data

        total_data = len(self.data)
        remainder = total_data % k

        clusters_data = []
        memberships = []
        for _ in range(k):
            clusters_data.append(np.matrix.copy(self.data))
            cluster_len = total_data//k
            if remainder:
                cluster_len += 1
                remainder -= 1
            memberships.append(cluster_len)
            self.data = np.roll(self.data, cluster_len, axis=0)

        self.clusters = []
        for i in range(k):
            self.clusters.append(
                FuzzyCluster(clusters_data[i], memberships[i]))

    def __str__(self):
        out = ""
        for i, cluster in enumerate(self.clusters):
            out += "\nCluster: " + str(i)
            out += cluster.__str__()
        return out

    def compute_centroids(self):
        """
        an update function
        computes new cluster centroids based on assignment
        """
        pass

    def compute_membership(self):
        """
        an update function
        computes similar but better membership assignment
        """

    def iterate(self):
        pass

    def reload(self, k=4):
        """
        restarts with current data
        """
        self.__init__(self.data, k=k)

    def add_data(self, data):
        """
        adds data to clustering system
        """
        # dump all data in first cluster
        self.clusters[0].data = np.concatenate(
            self.clusters[0].data, data)
        self.clusters[0].membership = np.concatenate(
            self.clusters[0].membership, np.ones((1, len(data))))

        # update remaining clusters
        for cluster in self.clusters[1:]:
            cluster.data = np.concatenate(cluster.data, data)
            cluster.membership = np.concatenate(
                cluster.membership, np.zeros((1, len(data))))

    def reduce(self, resolution: int):
        """
        reduces the amount of data without significant loss in information
        """


if __name__ == "__main__":
    def random_point():
        return np.random.randint(0, high=10, size=(2, 1))

    points = []
    for _ in range(25):
        points.append(random_point())
    for _ in range(25):
        points.append(random_point() + 15)

    clustering = FuzzyClustering(points, k=2)

    print(points)
    for _ in range(20):
        print(clustering)
