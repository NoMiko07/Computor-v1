import sys
from EquationClass import EquationSide
import re
import math

from colorama import init, Fore


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
            #print(Fore.RESET +'comparaison',longuest_equation_key, shortest_equation_key)
            if longuest_equation_key == shortest_equation_key:              
                #print(Fore.RED +'dans le if',longuest_equation_key, shortest_equation_key)
                #print('pendant le if',longuest_equation_value, shortest_equation_value)
                newvalue = longuest_equation_value - shortest_equation_value
                if newvalue == 0:
                    key_to_delete.append(longuest_equation_key)
                longuest_equation[longuest_equation_key] = newvalue
               # print(Fore.YELLOW +'apres le if newvalue',newvalue)
                # print(Fore.YELLOW +'apres le if',longuest_equation[longuest_equation_key])
        
    for key in key_to_delete:
        del longuest_equation[key]
    return longuest_equation

    

def print_output(reduced_equation):
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
        print((f'{coefficient}' if coefficient != 1 else '') +
              (' * ' if coefficient > 1 and power != 0 else '')  + 
              (f'X^{power}' if power != '0' else ''), end=' ')
        degree = power
        if first > 0:
            first = 0
    print("= 0")
    print(f"Polynomial degree: {degree}")
    if int(degree) > 2:
        return print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif int(degree) == 2:
        a, b, c  = get_abc(reduced_equation)
        solving_equation_second_degree(a, b, c)
        #print('a b c', a , b , c)

def get_abc(equation):
    a = equation.get('2', 0)
    b = equation.get('1', 0)
    c = equation.get('0', 0)
    return a, b , c    
    
def solving_equation_second_degree(a, b, c):
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
        print(f"Discriminant equal {delta} , the only solution is ", "{:.6f}".format(x0))
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Discriminant is strictly positive ({delta}), the two solutions are:", 
              '\n', "{:.6f}".format(x1) , '\n', "{:.6f}".format(x2))
        
        

def main():
    """ remove comment after parsing
    if len(sys.argv) > 1:
        argument = sys.argv[1]
    else:
        print("no argument")
        return
    """
    
    equation_str = '0 - 4 * X^1 + 4* X^2 = -1 * X^0'
    # ------ for later -------
    #left_equation = EquationSide(sys.argv[1], 'Left')
    #right_equation = EquationSide(sys.argv[1], 'Right')
    
    
    left_equation = EquationSide(equation_str, 'Left')
    right_equation = EquationSide(equation_str, 'Right')
    
    #print("equation is " + equation_str)
    #print(f"left argument is {left_equation.splitedEquation}")
    #print(f"right argument is {right_equation.splitedEquation}")


    
    #print("left", left_equation.splitForCoefPol())
    #print("right", right_equation.splitForCoefPol())
    
    if left_equation.length > right_equation.length:
        left_equation.coefPol = equation_balancing(left_equation.coefPol, right_equation.coefPol)
    else:
        right_equation.coefPol = equation_balancing(right_equation.coefPol, left_equation.coefPol)
    
    print(equation_str)
    print_output(left_equation.coefPol)

if __name__ == "__main__":
    main()