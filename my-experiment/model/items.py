from helper_functions import gen_attributes
import numpy as np

class Item:
    def __init__(self, id, isInARM=False):
        self.id = id
        self.attributes = gen_attributes()
        #self.last_price = 0
        self.inARM = isInARM

        prices = np.random.rand(2)

        self.floorPrice = np.min(prices)
        self.cielPrice = np.max(prices)

    def swap(self, price):
        """
        moves the item in or out of the ARM with an associated price

        if its add liquidity price is added to R and item i is added
        if its remove liquidity price is removed from R and item i is removed
        if its swap the item out then price is added to R and item i is taken
        if its swap the item in then price is removed from R and the item i is added

        """
        #self.last_price = price
        #print(self.for_sale)
        self.inARM = not(self.inARM) #switches its sign
        self.floorPrice = np.min([price, self.floorPrice])
        self.cielPrice = np.max([price, self.cielPrice])
    
    def dump(self):
        """
        return all attributes as a dictionary
        """
        data = {
            "id": self.id,
            "attributes": self.attributes,
            "inARM": self.inARM,
            "floorPrice":self.floorPrice,
            "cielPrice":self.cielPrice
        }
        return data

    # def compare(self, other):

    #     return np.max(np.abs(self.attributes-other.attributes))