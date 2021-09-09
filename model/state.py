from .model.learning import Model
from .model.items import Item

genesis_state = {
    "reserve": 10,
    "items": {0:Item(0)},
    "model": Model(10) #10 is the number of feature in our attribute space
}
