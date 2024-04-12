import sys
from EquationClass import EquationSide
import re


from colorama import init, Fore


def reduce_equation(longuest_equation, shortest_equation):
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

def main():
    """ remove comment after parsing
    if len(sys.argv) > 1:
        argument = sys.argv[1]
    else:
        print("no argument")
        return
    """
    
    equation_str = '-8.5 + X^1 - X^2 + 2 * X^3 = X - 2 * X^2'
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
        left_equation.coefPol = reduce_equation(left_equation.coefPol, right_equation.coefPol)
    else:
        right_equation.coefPol = reduce_equation(right_equation.coefPol, left_equation.coefPol)
    
    print(equation_str)
    print_output(left_equation.coefPol)

if __name__ == "__main__":
    main()