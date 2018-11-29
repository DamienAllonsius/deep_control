"""
Author : Damien Allonsius & Simone Totaro
Date : 29/11/2018
Python Version : 3.6

Main function for deep control. 
Take a PDE equation (for example parabolic)
and discretize it. For the moment : dimension space = 1.

The code works this way:
_ Select an initial condition on the mesh
_ Take a random control v
_ Take epsilon >0

_ While error(v) > epsilon do:

_ Inject in the system a control v : you get the solution at time T : y(T).
_ Third you compute the loss function : error(v) = y^2(T) (for the moment).
_ Finally you use a Neural Network to compute a better control.
"""
import numpy as np
from neural_network import *
from mesh import *
from equation import *
from test_case import *

test_case = TEST_CASE_1
x_uniform = np.linspace(test_case[DOMAIN][0], test_case[DOMAIN][1], test_case[POINT_X])
mesh = Mesh(x = x_uniform)   
# Intialise the control
control = #TODO with the mesh
equation = Equation(test_case, control, mesh)

neural_network = Neural_network(equation.loss_function())

while neural_network.loss_value > test_case[EPSILON]:
    # update the control variable of the equation
    equation.control = neural_network.one_step_improvement(control)

    # update the variable y of equation by computing the solution
    equation.compute_solution()

    # compute the loss_function
    loss  = equation.loss_function()

    # update the loss parameter of the neural network
    neural_network.loss_value = loss
