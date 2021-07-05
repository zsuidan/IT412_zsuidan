def divideTwoNumbers(passed_list):
    """Proccesses a list of numbers, and divides one number by the other
    Arguments:
        passed_list [list of dictionaries] -- each dictionary has the format of {top_number: int, botttom_number: int}
    Returns:
        a list of values obtained when we divide top_number by bottom_number for each dictionary
    """

    divide_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 2

    for divide_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(divide_vals["top_number"])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int(divide_vals["bottom_number"])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False

        if numbers_ok:
            divide_result = passed_number1 / passed_number2
            divide_results.append(divide_result)
    
    return divide_results

def multiplyTwoNumbers(passed_list):
    """Proccesses a list of numbers, and multiplies one number by the other
    Arguments:
        passed_list [list of dictionaries] -- each dictionary has the format of {top_number: int, botttom_number: int}
    Returns:
        a list of values obtained when we multiply top_number by bottom_number for each dictionary
    """

    multiply_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 2

    for multiply_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(multiply_vals["top_number"])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int(multiply_vals["bottom_number"])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False

        if numbers_ok:
            multiply_result = passed_number1 * passed_number2
            multiply_results.append(multiply_result)
    
    return multiply_results