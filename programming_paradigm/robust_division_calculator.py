def safe_divide (numerator, denominator):
    

    try:
        numerator_convers = float(numerator)
        denominator_convers = float(denominator)

        result = (numerator_convers / denominator_convers)
        return f'The result of the division is {result}'

    except ZeroDivisionError:
        return f'Error: Cannot divide by zero.'
    
    except ValueError:
        return f'Error: Please enter numeric values only.'