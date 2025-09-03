import sys
from EquationClass import EquationSide
from fractions import Fraction

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

def sqrt(x: float, precision: float = 1e-10) -> float:
    if x < 0:
        raise ValueError("x can't be negative")
    if x == 0:
        return 0.0
    
    r = x
    while abs(r * r - x) > precision:
        r = (r + x / r) / 2
    return r
    

def print_output(reduced_equation, freeform):
    first = 1
    degree = '0'
    
    print("Reduced form: ", end='')

    if not reduced_equation:
        print("0 = 0")
        print("Any real number is a solution.")
        return

    if all(k == '0' for k in reduced_equation) and reduced_equation.get('0', 0) != 0:
        coef = reduced_equation['0']
        print(f"{coef} = 0")
        print("Polynomial degree: 0")
        print("No solution.")
        return

    for power, coefficient in reduced_equation.items():
        if first == 0:
            if coefficient < 0:
                coefficient = abs(coefficient)
                print("-", end=' ')
            else:
                print("+", end=' ')
        if power in freeform and freeform[power] == False:
            if power == '1':
                print(f'{coefficient} * X', end=' ')
            else:
                print(f'{coefficient}', end=' ')
        else:
            print(f'{coefficient} * X^{power}', end=' ')
        degree = power
        if first > 0:
            first = 0

    print(f"= 0\nPolynomial degree: {degree}")

    if int(degree) > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif int(degree) == 2:
        a, b, c = get_abc(reduced_equation)
        solve_equation_second_degree(a, b, c)
    elif int(degree) == 1:
        a, b, c = get_abc(reduced_equation)
        solve_equation_first_degree(b, c)
    else:
        if reduced_equation.get('0', 0) == 0:
            print("All real numbers are solutions.")
        else:
            print("No solution.")


def get_abc(equation):
    a = equation.get('2', 0)
    b = equation.get('1', 0)
    c = equation.get('0', 0)
    return a, b , c    

def format_fraction(num, den):
    frac = Fraction(num).limit_denominator() / Fraction(den).limit_denominator()
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"

def solve_quadratic(a, b, delta):
    real_part = format_fraction(-b, 2*a)
    sqrt_delta = (-delta) ** 0.5
    if abs(sqrt_delta - round(sqrt_delta)) < 1e-9:
        imag_part = format_fraction(((-delta)**0.5), 2*a)
        print(f"{real_part} + {imag_part}i")
        print(f"{real_part} - {imag_part}i")
    else:
        sqrt_delta = int(-delta)
        denom = format_fraction(2*a, 1)
        print(f"{real_part} + √{sqrt_delta}/{denom}i")
        print(f"{real_part} - √{sqrt_delta}/{denom}i")

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
        print(f"Discriminant is strictly negative ({delta}), the two complex solutions are:")
        solve_quadratic(a, b, delta)
    elif delta == 0:
        x0 = -b/(2 * a)
        print(f"Discriminant equal {delta} , the only solution is {x0:.6f}")
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print(f"Discriminant is strictly positive ({delta}), the two solutions are:\n{x1:.6f}\n{x2:.6f}")

def solve_equation_first_degree(a, b):
    x = -b / a
    print("The solution is:")
    print(x)

def main():
    try:
        equation_str = ''
        if len(sys.argv) > 1:
            equation_str = sys.argv[1]
        else:
            print("No argument provided")
            return    

        left_equation = EquationSide(equation_str, 'Left')
        right_equation = EquationSide(equation_str, 'Right')

        if left_equation.length >= right_equation.length:
            left_equation.coefPol = equation_balancing(left_equation.coefPol, right_equation.coefPol)
            print_output(left_equation.coefPol, left_equation.freeForm)
        else:
            right_equation.coefPol = equation_balancing(right_equation.coefPol, left_equation.coefPol)
            print_output(right_equation.coefPol, right_equation.freeForm)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()