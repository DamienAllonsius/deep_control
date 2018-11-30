"""
The TEST_CASE variable is a dictionary that contains all the parameters of the system
"""

TEST_CASE_1 = {}


"""
A first test case with the Heat Equation.
"""

TEST_CASE_1.update(
    SPACE_DIMENSION = 1,
    PARABOLIC = True,
    EPSILON = 10^(-3),             
    INITIAL_CONDITION = 1,
    DOMAIN = [0,1],
    BOUDARY_CONTROL = True,
    GAMMA = 1,
    Q = 0,
    POINT_X = 100,
    POINT_T = 100,
    T = 1)

"""
We can also take fancy diffusion and potential parameters.
TODO
"""
#qString="x**2"
#gammaString="np.cos(x)+1"

#def q(x):
#    return eval(qString)

#def gamma(x):
#    return eval(gammaString)

