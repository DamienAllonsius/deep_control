"""
Author : Damien Allonsius
Date : 29/11/2018
Python Version : 3.6

This is the equation, seen as a black box.
As input, he takes the parameter of a test case and a control.
The function : loss_function returns the loss function.
"""
import numpy as np

class Equation(object):

    def init(self, test_case, control, mesh):
        self.test_case = test_case
        self.control = control
        self.y = None

    def compute_solution(self):
        """
        Compute the solution at time T.
        This is the black box. All the job is done here.
        update self.y
        TODO
        """

    # def compute_norm_control(self):
    #     """
    #     Compute the L2 norm of the control
    #     """
    #     return np.linalg.norm(v,2)
        
    def loss_function(self):
        """
        Return the value of the loss function with respect to v.
        (Basic loss_function for the moment)
        """
        return np.linalg.norm(self.y[-1], 2)
