from model.model.helper_functions import quadratic_form
import numpy as np

class Model:
    def __init__(self, n):
        """
        n is the number of attributes

        super lame linear model to start
        y = x'Ax
        """
        self.A = np.eye(n,n)

    def update(self, x, y):
        """
        learning logic here

        change A such that
        y = x'Ax
        """

        #naive rescale (this is a dummy method)
        scale = self.predict(x)
        self.A = y*self.A/scale 

    def predict(self, x):

        return quadratic_form(x, self.A)