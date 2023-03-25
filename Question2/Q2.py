import pandas as pd

def generate_model(x):
    '''
    Your logic goes here 
    '''

def code_driver(train=False):
    train_data = pd.read_csv("train.csv")
    test_data = pd.read_csv("test.csv")
    if train == True:
        model = generate_model(train_data)
        pd.to_pickle(model,'model.pkl')
    else:
        model = pd.read_pickle('model.pkl')
    
    test_results = model.predict(test_data)
    test_results.to_csv("submission.csv")
 
if __name__ == "__main__":
    code_driver(train=True) 