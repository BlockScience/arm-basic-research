from items import Item
import numpy as np

from sklearn.cluster import AgglomerativeClustering

class Collection:
    def __init__(self, n, k=10):
        self.items = {i:Item(i, bool(np.random.randint(0,2))) for i in range(n)}
        
        attribute_vectors = np.array([i.attributes for i in self.items.values()])
        #vector_weights = np.array([i.cielPrice/2+i.floorPrice/2 for i in self.items.values()])

        self.clustering = AgglomerativeClustering(n_components=k).fit(attribute_vectors)

    def update_clusters(self):
        attribute_vectors = np.array([i.attributes for i in self.items.values()])
        #vector_weights = np.array([i.cielPrice/2+i.floorPrice/2 for i in self.items.values()])
        self.clustering = AgglomerativeClustering(n_components=self.clustering.n_clusters).fit(attribute_vectors)