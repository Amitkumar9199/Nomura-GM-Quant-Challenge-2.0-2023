def rec(digits, pos, sum1, sum2,val):
    if pos == len(digits):
        if sum1 + sum2 == val:
            return True
        return False
    return rec(digits, pos+1, sum1+sum2, digits[pos],val) or rec(digits, pos+1, sum1, sum2*10 + digits[pos],val)
def is_fancy_number(num):
    square = num ** 2
    digits = list(map(int, str(square)))
    return rec(digits, 0, 0, 0,num)

def generate_result(x):
    '''
    Your logic goes here 
    '''
    count = 0
    for num in range(1, x+1):
        if is_fancy_number(num):
            count += 1
    return count

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