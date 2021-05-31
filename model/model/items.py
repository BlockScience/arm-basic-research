from .helper_functions import gen_attributes
import numpy as np

class Item:
    def __init__(self, id):
        self.id = id
        self.attributes = gen_attributes()
        #self.last_price = 0
        self.for_sale = False

    def swap(self):
        """
        moves the item in or out of the ARM with an associated price

        if its add liquidity price is added to R and item i is added
        if its remove liquidity price is removed from R and item i is removed
        if its swap the item out then price is added to R and item i is taken
        if its swap the item in then price is removed from R and the item i is added

        """
        #self.last_price = price
        print(self.for_sale)
        self.for_sale = not(self.for_sale) #switches its sign

    def compare(self, other):

        return np.max(np.abs(self.attributes-other.attributes))
