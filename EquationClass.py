import re
from collections import OrderedDict

class EquationSide:
    """
    A class which takes a polynomial equation as an argument and 
    splits it into its left-hand side or right-hand side depending on user preference.

    Methods:
    __init__(argument: str, side: str): Initializes an EquationSide object.
    split_LorR(self, side: str): Splits the equation into its left or right side.
    """
    def __init__(self, equation: str, side: str):
        """
        Initializes an EquationSide object.

        Parameters:
        equation (str): The polynomial equation to be processed.
        side (str): Indicates whether to process the left-hand side ('left') or the right-hand side ('right') of the equation.
        """
        self.splitedEquation: str = self.split_LorR(equation, side)  # Full equation
        self.freeForm: OrderedDict[str, bool] = {}
        self.coefPol: OrderedDict[str, float] = self.splitForCoefPol()  # Ordered Dictionary to store the powers of 'x' in the equation
        self.length: int = len(self.coefPol)
        
    def split_LorR(self, equation: str, side: str):
        """
        Splits the equation into its left or right side.

        Parameters:
        side (str): Indicates whether to process the left-hand side ('left') or the right-hand side ('right') of the equation.
        """
        parts = equation.split("=")
        
        if side.lower() == 'left':
            return parts[0].strip()
        else:
            return parts[1].strip()
        
    def splitForCoefPol(self):
        coefPol: OrderedDict[str, float] = OrderedDict()
        terms = re.split(r'\s*([+-])\s*', self.splitedEquation)
        if terms[0] == '':
            terms.pop(0)
        i = 0
        if terms[0] == '-':
            i = 1
        
        positionX0 = -1
        positionX1 = -1
        for item in terms:
            if positionX0 == -1:
                positionX0 = item.find('X^0')
            if positionX1 == -1:
                positionX1 = item.find("X^1")
        self.freeForm['0'] = True if positionX0 != -1 else False
        self.freeForm['1'] = True if positionX1 != -1 else False
        
        while i < len(terms):
            if i >= 1:
                terms[i] = terms[i - 1] + terms[i]
            coefficient = self.find_coef(terms[i])
            power = self.find_power((terms[i]))
            if power in coefPol:
                coefPol[power] += coefficient
            else:
                coefPol[power] = coefficient
            i+=2
        return coefPol

    def find_coef(self, formula: str) -> float:
        """
        Find the coefficient of the formula and return it as a float. 
    
        Parameters:
        formula (str): The formula from which to extract the coefficient.
        
        Note:
        If the coefficient is not explicitly specified in the formula, 
        this function returns either 1 or -1 depending on the presence of a minus sign ('-') at the beginning of the formula.
        """
        neg = ''
        if formula.startswith('-'):
            neg = '-'
        position = formula.find('*')
        numbers = re.findall(r'-?\d*\.?\d+', formula)
        
        if position != -1:
            return float(formula.split('*')[0])
        elif numbers and (len(formula) < 2 or (formula[0] != 'X' and formula[1] != 'X')):
                return float(numbers[0])
        else:
            return float(neg + '1')

    def find_power(self, formula: str) -> str:        
        """
        find the power of the formula and return it as a string.

        Parameters
        formula (str): The formula from which to extract the power.

        Note:
        If the coefficient is not explicitly specified in the formula, 
        this function returns 1
        """
        
        positionX = formula.find('X')
        positionXPower = formula.find("X^")
        
        if positionXPower != -1:
            return formula.split('X^')[1]
        elif positionX != -1:
            return '1'
        else:
            return '0'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        