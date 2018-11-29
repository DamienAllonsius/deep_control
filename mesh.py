"""
Author : Damien Allonsius
Date : 29/112018
Python Version : 3.6

The Mesh class.
Can handle any type of non regular mesh.
For the moment : uniform meshes.
"""
import numpy as np
class Mesh(object):
    """
    This class represents a mesh on a one dimensional interval (0,L).
    By default L=1
    This class contains : 
    _ A mesh parameter h=(h_1,h_2,...,h_N)
    _ The mesh points x=(x_1=0,x_2,...,x_(N+1),x_(N+2)=L)
    _ The dual mesh parameter h=(h_(1/2),h_(1/2+1),...,h_(1/2+N))
    _ The dual mesh points x=(x_(1/2), x_(1/2+1),...,x_(1/2+N))
    """
    def __init__(self, L = None, hDual = None, x = None):
       
        if L is None:
            L = 1
        self.L = L
        
        if (hDual is None) and (x is None):
            raise ValueError('You must specify x or dual h')
        
        if x is None:
            x = self.makeMeshPoints(hDual)
        self.x = np.array(x)
        
        self.hDual = self.makeDualMeshParameter(x)
        self.xDual = self.makeDualMeshPoints()
        self.h = self.makeMeshParameter()

    def makeDualMeshParameter(self, x):
        '''
        return the dual mesh parameter (h_(1/2), h_(1/2+1),...,h_(1/2+N))
        '''
        return np.array(x[1:] - x[:-1])

    def makeMeshPoints(self, hDual):
        '''
        return the mesh points  (x_1=0,x_2,...,x_{N+1},x_{N+2}=1)
        '''
        x = [0]
        for h in hDual:
            x.append(x[-1]+h)
        x = np.array(x)
        x = x / x.item(-1)
        return x

      
    def makeDualMeshPoints(self):
        '''
        return the dual mesh points x=(x_(1/2), x_(1/2+1),...,x_(1/2+N))
        '''
        return (self.x[1:] + self.x[:-1]) / 2

    
    def makeMeshParameter(self):
        '''
        return the mesh parameter h=(h_1,h_2,...,h_N)
        '''
        return self.xDual[1:] - self.xDual[:-1]

