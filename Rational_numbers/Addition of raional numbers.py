from fractions import Fraction

def add_rational_numbers(num1, num2):
    # Convert the input numbers to fractions
    fraction1 = Fraction(num1)
    fraction2 = Fraction(num2)
    
    # Check if the denominators are the same
    if fraction1.denominator == fraction2.denominator:
        # Add the numerators if the denominators are the same
        result = fraction1 + fraction2
        return result
    else:
        return "The denominators must be the same."

# Example usage:
num1 = "3/5"
num2 = "1/5"

result = add_rational_numbers(num1, num2)
print("The sum of the rational numbers is:", result)
