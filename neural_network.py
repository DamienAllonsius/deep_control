"""
Simone Totaro
"""

import numpy as np

class Neural_network(object):
    """
    The neural network approximates the control.
    The loss function is given by
    """

    def __init__(self, loss_value):
        self.loss_value = loss_value
    
    def one_step_improvement(self, v):
        """
        Returns the new improved v after one step of iteration.
        """
        return v
