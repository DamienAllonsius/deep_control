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
x_uniform = np.linspace(test_case['DOMAIN'][0], test_case['DOMAIN'][1], test_case['POINT_X'])
mesh = Mesh(x = x_uniform)


# Intialise the equation control
equation = Equation(test_case, mesh)
neural_network = Neural_network(equation.get_loss_value())
count = 0

while neural_network.loss_value > test_case['EPSILON']:
    count += 1
    
    # update the control variable of the equation
#    equation.control = neural_network.one_step_improvement(equation.control)

    # update the y variable of equation by computing the solution with the new control
    equation.compute_solution()

    # use the loss function to compute the loss value
    loss  = equation.get_loss_value()

    # print the result
    print('iteration : ' + str(count) + '. Loss value: ' + str(loss))
    
    # update the loss value of the neural network
    neural_network.loss_value = loss


# plot the solution
user_interface = UI(test_case, mesh, equation.y)
