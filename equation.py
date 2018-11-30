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
    
    def __init__(self, test_case, mesh):
        self.test_case = test_case
        self.control = self.get_random_control()
        self.y = None

    def get_random_control(self):
        """
        Initialise the control with random values between 0 and 1.
        """
        if self.test_case['SPACE_DIMENSION'] == 1:
            if self.test_case['BOUDARY_CONTROL']:
                return np.random.rand()
            #TODO : else
            
    def compute_solution(self):
        """
        Compute the solution at time T.
        This is the black box. All the job is done here.
        update self.y
        TODO
        """
        if self.test_case['PARABOLIC']:
            # here the equation reads : y_t - \Delta y = v
            # we apply a basic finite different discretization on the mesh
        return 
    # def compute_norm_control(self):
    #     """
    #     Compute the L2 norm of the control
    #     """
    #     return np.linalg.norm(v,2)
        
    def get_loss_value(self):
        """
        Return the value of the loss function with respect to v.
        (Basic loss_function for the moment)
        """
        return np.linalg.norm(self.y[-1], 2)
