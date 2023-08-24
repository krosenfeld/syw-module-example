import numpy as np 

def generate_random_numbers(n):
    """ stand-in for np.random.random """
    return np.random.random(n)

class ExampleClass():
    """An example class

    This example shows example docstring, constructor, and method

    Args:
        arr (:py:class:`~numpy.ndarray`): An array
        b (float, optional): A float
    """

    def __init__(self, arr, b=1):
        self.arr = arr
        self.b = b

    def add_b(self):
        self.arr += self.b

