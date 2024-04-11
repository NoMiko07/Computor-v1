import sys
from EquationClass import EquationSide
import re

def main():
    """ remove comment after parsing
    if len(sys.argv) > 1:
        argument = sys.argv[1]
    else:
        print("no argument")
        return
    """
    
    equation_str = '-8.5 - X^1 - X^2 + 2 * X^3 = X'
    # ------ for later -------
    #EquationLeft = EquationSide(sys.argv[1], 'Left')
    #EquationRight = EquationSide(sys.argv[1], 'Right')
    
    
    EquationLeft = EquationSide(equation_str, 'Left')
    EquationRight = EquationSide(equation_str, 'Right')
    
    #print("equation is " + equation_str)
    print(f"left argument is {EquationLeft.splitedEquation}")
    #print(f"right argument is {EquationRight.splitedEquation}")


    #print("terme")
    print(EquationLeft.coefPol)
    
    for key ,value in EquationLeft.coefPol.items():
        print('key ------>', key, ' | value ----->', value)
    #print(EquationRight.splitForCoefPol())



if __name__ == "__main__":
    main()