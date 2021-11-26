import numpy as np

def gen_attributes(n=25):
    """
    n random bits make up the attributes in the dummy model
    """
    return np.random.rand(0,2,size=n)

def gen_context(n=10):
    """
    method returns a random matrix which can be used to produce private prices over a bunch of items
    """

    return np.random.randint(-3,4,size=(n,n))

def is_for_sale(items, flip=False):
    if flip:
        keys = list(items.keys())
        return [ k for k in keys if not(items[k].for_sale) ]
    else:
        keys = list(items.keys())
        return [k for k in keys if items[k].for_sale ]

def quadratic_form(x, A):

    pre = A.dot(x)
    val = pre.dot(x) 

    return val