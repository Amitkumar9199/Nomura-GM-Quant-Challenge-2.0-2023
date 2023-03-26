import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier 
import numpy as np

def transform_data(df):
    '''
        transform_data(df) -> X
        df: Dataframe
        X: Transformed Dataframe
        fillna with mean
        fillna with mode
        add new column diff_high_low = high - low
        add new column diff_open_close = open - close
        add new column ratio_currvol_prevvol = volume/prev volume
        add new column ratio_diffhighclose_difflowclsoe = (high-close)/(low-close)
        drop high, low, open, close, volume, prev volume
        return X after scaling
    '''    
    df.fillna(df.mean(), inplace=True)
    df.fillna(df.mode().iloc[0], inplace=True)
    df['diff_high_low'] = df['high'] - df['low']
    
    df['diff_open_close'] = df['open'] - df['close']
    
    df['ratio_currvol_prevvol']=df['volume']/df['prev volume']
    
    df['ratio_diffhighclose_difflowclsoe']=(df['high']-df['close'])/(df['low']-df['close'])
    df['ratio_diffhighclose_difflowclsoe'].replace(np.inf, np.nan, inplace=True)
    df['ratio_diffhighclose_difflowclsoe'].replace(-np.inf, np.nan, inplace=True)
    df['ratio_diffhighclose_difflowclsoe'].fillna(df['ratio_diffhighclose_difflowclsoe'].median(), inplace=True)

    df.drop(['high','low','open','close','volume','prev volume'],axis=1,inplace=True)
    X=df.filter(['ratio_diffhighclose_difflowclsoe','return','volatility','diff_high_low', 'diff_open_close', 'ratio_currvol_prevvol'], axis = 1)
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    return X

def generate_model(x):
    '''
        generate_model(x) -> rf
        x: Dataframe
        rf: Random Forest Classifier
        return rf after training on x
    '''
    train_data = x
    y_train = train_data['next month return sign']
    train_data.drop(['next month return sign'],axis=1,inplace=True)
    X_train = transform_data(train_data)

    rf=RandomForestClassifier(random_state=42)
    rf.fit(X_train,y_train)
    return rf

def code_driver(train=False):
    train_data = pd.read_csv("train.csv")
    test_data = pd.read_csv("test.csv")
    if train == True:
        model = generate_model(train_data)
        pd.to_pickle(model,'model.pkl')
    else:
        model = pd.read_pickle('model.pkl')
    
    test_data = transform_data(test_data) # Transforming test data

    test_results = model.predict(test_data)
    
    test_results = pd.DataFrame(test_results) # Converting to dataframe
    
    test_results.to_csv("submission.csv", index=False,header=False) 
 
if __name__ == "__main__":
    code_driver(train=True) 