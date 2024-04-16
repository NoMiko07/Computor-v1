import sys
from EquationClass import EquationSide
import re
import math



def equation_balancing(longuest_equation, shortest_equation):
    """ Balance the equation so that the result is equal to 0.

   This function takes two equations as input, 'longuest_equation' and 'shortest_equation',
   represented as dictionaries where keys are the powers of 'X' and values are the coefficients
   of each term. It subtracts corresponding terms from 'longuest_equation' and 'shortest_equation'
   to ensure that the resulting equation is balanced and equals 0.

   Parameters:
   - longuest_equation (OrderedDict[str, float]): The longest equation.
   - shortest_equation (OrderedDict[str, float]): The shortest equation.

   Returns:
   - OrderedDict[str, float]: The balanced equation.
   """
    key_to_delete = []
    for longuest_equation_key ,longuest_equation_value in longuest_equation.items():
        for shortest_equation_key ,shortest_equation_value in shortest_equation.items():
            if longuest_equation_key == shortest_equation_key:
                newvalue = longuest_equation_value - shortest_equation_value
                if newvalue == 0:
                    key_to_delete.append(longuest_equation_key)
                longuest_equation[longuest_equation_key] = newvalue
    
    for power, coef in shortest_equation.items():
        if power not in longuest_equation:
            if shortest_equation[power] < 0:
                longuest_equation[power] =  abs(shortest_equation[power])
            else:
                longuest_equation[power] =  - shortest_equation[power]
        
    for key in key_to_delete:
        del longuest_equation[key]
    
    sorted_dict = dict(sorted(longuest_equation.items()))
    return sorted_dict

    

def print_output(reduced_equation, freeform):
    first = 1
    degree = '0'
    
    print("Reduced form: ", end='')
    
    for power, coefficient in reduced_equation.items():
        if first == 0:
            if coefficient < 0:
                coefficient = abs(coefficient)
                print("-", end=' ')
            else:
                print("+", end=' ')
        if power in freeform and freeform[power] == False:
            if power == '1':
                print(f'{coefficient} * X', end = ' ')
            else:
                print(f'{coefficient}', end = ' ')
        else:
            print(f'{coefficient} * X^{power}', end = ' ')
        degree = power
        if first > 0:
            first = 0
    print(f"= 0\nPolynomial degree: {degree}")
    if int(degree) > 2:
        return print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif int(degree) == 2:
        a, b, c  = get_abc(reduced_equation)
        solve_equation_second_degree(a, b, c)
    elif int(degree) == 1:
        a, b, c = get_abc(reduced_equation)
        solve_equation_first_degree(b, c)
    else:
        print("The equation can't be solved")

def get_abc(equation):
    a = equation.get('2', 0)
    b = equation.get('1', 0)
    c = equation.get('0', 0)
    return a, b , c    
    
def solve_equation_second_degree(a, b, c):
    """ 
    to solve a second degree equation we need to get the discriminant(Δ).
    Δ = b² - 4ac
    if:
        Δ < 0 there is no solution
        Δ = 0 there is 1 solution
        Δ > 0 2 solution 
    """
    delta = pow(b, 2) - (4 * a * c)
    if delta < 0:
        print(f"Discriminant is strictly negative ({delta}) , there is no solution")
    elif delta == 0:
        x0 = -b/(2 * a)
        print(f"Discriminant equal {delta} , the only solution is {x0:.6f}")
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Discriminant is strictly positive ({delta}), the two solutions are:\n{x1:.6f}\n{x2:.6f}")
        
        
        
def solve_equation_first_degree(a, b):
    x = -b / a
    print("The solution is:")
    print(x)

def main():
    equation_str = ''
    if len(sys.argv) > 1:
        equation_str = sys.argv[1]
    else:
        print("no argument")
        return    
    
    left_equation = EquationSide(equation_str, 'Left')
    right_equation = EquationSide(equation_str, 'Right')
    
    
    if left_equation.length >= right_equation.length:
        left_equation.coefPol = equation_balancing(left_equation.coefPol, right_equation.coefPol)
        print_output(left_equation.coefPol, left_equation.freeForm)
    else:
        right_equation.coefPol = equation_balancing(right_equation.coefPol, left_equation.coefPol)
        print_output(right_equation.coefPol, right_equation.freeForm)
    

if __name__ == "__main__":
    main()