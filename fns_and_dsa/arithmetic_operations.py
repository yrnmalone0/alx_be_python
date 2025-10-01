def perform_operation(num1, num2, operation):
    """
        Perform basic arithmetic on two numbers:

        Arguments:
            num1(float) - first number
            num2(float) - second number
            operation(str) - accepts four values(add,subtract,multiply,divide)
        
        Returns: A floating number after any other arithmetic ops
    
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print(f"The value of {num1} cannot be divisible by zero(0)")
        return num1 / num2
    else:
        print("An error occured, please try again!!")