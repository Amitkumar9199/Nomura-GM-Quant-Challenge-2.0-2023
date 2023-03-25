def sin(x):
    """
    Computes the sine of x in degrees using the Maclaurin series expansion
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    """
    x =( (x % 360) + 360 ) % 360 # convert to range [0, 360)
    x = x * (3.14159265359 / 180) # convert to radians
    result = term = x
    i = 1
    while abs(term) >= 1e-10:
        term *= ((-1 * (x**2)) / ((2 * i) * (2 * i + 1)))
        result += term
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
    # print(generate_result(0))       # Output: 1
    # print(generate_result(30))      # Output: 0.5
    # print(generate_result(45))      # Output: 0.6366197723675814
    # print(generate_result(90))      # Output: 1.5707963267948966
    # print(generate_result(180))     # Output: 0.01745240643728351
    # print(generate_result(360))     # Output: 0.00030517578125
