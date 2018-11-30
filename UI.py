"""
Author : Damien Allonsius
Date : 30/11/2018
Python Version : 3.6

This is the user interface.
Make an animation and plot the solution
"""
#import mathplotlib

class UI(object):
    
    def __init__(self, test_case, mesh, solution):
        self.test_case = test_case
        self.mesh = mesh
        self.solution = solution
