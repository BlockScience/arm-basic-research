from typing import Collection
# from items import Item
import numpy as np
from collection import Collection

n=100
k = 10

items = Collection(n)

genesis_state = {
    "collection":  items,
    "reserve": 100,
    "clusters": {},
    "basis":{}
}

## quicktest
# for i in genesis_state['collection'].items.values():
#     print(i.dump())

# coll = genesis_state['collection'].clustering

# print(coll.cluster_centers_)