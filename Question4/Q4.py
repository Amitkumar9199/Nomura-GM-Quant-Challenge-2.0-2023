def generate_result(x):
    '''
    Your logic goes here 
    '''

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