def sin(x):
    """
    Computes the sine of x in degrees using the Taylor series expansion
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    """
    x =( (x % 360) + 360 ) % 360 # convert to range [0, 360)
    x = x * (3.14159265359 / 180) # convert to radians
    result = term = x
    i = 1
    while abs(term) >= 1e-10:
        # compute next term in series
        term *= ((-1 * (x**2)) / ((2 * i) * (2 * i + 1)))
        # add term to result
        result += term
        # increment counter for next term in series
        i += 1
    return result

def generate_result(x):
    """
    Computes the value of F(x) = sin(x)/x
    """
    if x == 0:
        return 1 # limt as x -> 0
    else:
        return sin(x) /x 

def code_driver():
    f_input = open("test_cases.txt","r")
    f_output = open("results.csv","w")
    test_cases = f_input.readlines()
    
    for i in test_cases:
        if i == '':
            continue
        res = str(generate_result((int(i))))
        f_output.write(res +'\n')

if __name__ == "__main__":
    code_driver()     
