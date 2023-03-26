import math

def count_special_pairs(x, y):
    count = 0 # initialize count
    # loop for all values from 1 to sqrt(x)
    for k in range(1, int(math.sqrt(x)) + 1):
        # max(0, min(y, x // k - 1) - k) is the number of values of b in the range [k+1, min(y, x // k - 1)] that satisfy a % b = a // b
        count += max(0, min(y, x // k - 1) - k)
    return count # return the count


def generate_result(x,y):
    '''
    Your logic goes here 
    '''
    count = count_special_pairs(x, y)
    return count

def code_driver():
    f_input = open("test_cases.txt","r")
    f_output = open("results.csv","w")
    test_cases = f_input.readlines()
    
    for i in test_cases:
        if len(i.split(',')) < 2:
            continue
        x,y = i.split(',')
        res = str(generate_result(int(x), int(y)))
        f_output.write(res +'\n')

if __name__ == "__main__":
    code_driver()   