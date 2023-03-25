cnt = []
def rec(digits, pos, sum1, sum2,val):
    '''
        rec :checks digits can be split into several numbers such that the sum of these is equal to the original number.
        digits array contains the digits of the square of the number
        pos is the current position in the digits array
        sum1 is the sum of the numbers we have added by splitting the digits array
        sum2 is the number we are currently building
        val is the original number's square
    '''
    if sum1 + sum2 > val: # not fancy
        return False
    if pos == len(digits): # end of digits
        if sum1 + sum2 == val: # if fancy
            return True
        return False
    # if we add the current digit to sum2 without updating total sum
    # if we make sum2=digit and update total sum1 = sum1 + sum2
    return rec(digits, pos+1, sum1+sum2, digits[pos],val) or rec(digits, pos+1, sum1, sum2*10 + digits[pos],val)

def is_fancy_number(num):
    '''
        is_fancy_number : checks if the number is fancy
    '''
    square = num ** 2
    digits = list(map(int, str(square))) # convert to array of digits
    return rec(digits, 0, 0, 0,num) # call recursive function

def generate_result(x):
    '''
    Your logic goes here 
    '''
    if x<=len(cnt):
        return cnt[x-1]
    count = 0
    if len(cnt) !=0:
        count = cnt[-1]
    for num in range(len(cnt)+1, x+1):
        if is_fancy_number(num):
            count += 1
        cnt.append(count)
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