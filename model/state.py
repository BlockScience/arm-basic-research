from .model.learning import Model
from .model.items import Item

genesis_state = {
    "reserve": 50,
    "items": {0:Item(0)},
    "model": Model(10) #10 is the number of feature in our attribute space
}
