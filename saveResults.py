"""
Author : Damien Allonsius
Date : 29/11/2018
Python Version : 3.6

Save the results in a spectified file
"""

from function import * 
import numpy as np
from numpy.linalg import norm as norm
import matplotlib.pyplot as plt

class Save:

    def __init__(self, pathFile, fileName):
        self.pathFile = pathFile
        self.fileName = fileName

    def saveData(self, time_vector, y, v):
        """
        TODO and TOFIX
        """
        f = open(self.pathFile + '/DATA_' + self.fileName,"w+")
        f.write("t y(t) v(t) \n")
        for k in range(len(time_vector)):
            f.write("%1.2E " % x[k])
            f.write("%1.2E \n" % y[k])
        f.close()

    def saveConfig(self, test_case):
        """
        TODO
        """        
        # f=open(self.pathFile+'/CONFIG_'+self.fileName,"w+")
        # f.write("gamma q slope Naccu Nmin Nmax Nstep\n")
        # f.write(gamma + " ")
        # f.write(q + " ")
        # f.write("%d " % Nstep)
        # f.close()

            
