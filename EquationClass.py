import re


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
        self.length: int = len(self.splitedEquation)  # Length of the full equation
        self.xPower: Dict[str, int] = {}  # Dictionary to store the powers of 'x' in the equation

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
        
    def splitForxPower(self):
        terms = re.split(r'\s*([+-])\s*', self.splitedEquation)
        if terms[0] == '':
            terms.pop(0)
        i = 0
        if terms[0] == '-':
            i = 1
        xPower = ''
        coefficient = 0
        while i < len(terms):
            coefficient = self.find_coef(terms[i])
            print("terme", terms[i])
            print(coefficient)
            i+=2
        
        return terms
    
    def find_coef(self, formula: str) -> int:
        position = formula.find('*')
        if position != -1:
            return int(formula.split('*')[0])
        else:
            return 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        