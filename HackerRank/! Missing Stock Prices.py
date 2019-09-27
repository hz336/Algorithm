# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import numpy as np
from scipy.interpolate import UnivariateSpline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier


def read_data(): 
    n = int(input())
    list_date = []
    list_price = []
    for i in range(n): 
        i_date, i_price = input().strip().split('\t')
        list_date.append(i_date)
        list_price.append(i_price)
    
    df = pd.DataFrame({'date': list_date, 'price': list_price})
    df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y %H:%M:%S")
    df['date'] = df['date'].astype(int)
    df['missing'] = df['price'].apply(lambda x: 1 if x.startswith('Missing') else 0)
    df_value = df[df['missing']==0].iloc[:, df.columns!='missing']
    df_missing = df[df['missing']==1].iloc[:, df.columns!='missing']

    return df_value, df_missing

def model(df_train, df_test): 
    df_train, df_val = train_test_split(df_train, test_size=0.05, random_state=0, shuffle=False)
    X_train, y_train = df_train.iloc[:, df_train.columns!='price'].values, df_train['price'].values
    X_test = df_test.iloc[:, df_test.columns!='price'].values
    
    # ## Model 1 - Univariate smoothing spline 
    # ml_spline = UnivariateSpline(df_train['date'].values, df_train['price'].values)
    # pred_sl = ml_spline(df_test['date'].values)
    # for pred in pred_sl:
    #     print(pred)

    # ## Model 2 - Linear Regression
    # ml_lr = LinearRegression()
    # ml_lr.fit(X_train, y_train)
    # pred_lr = ml_lr.predict(X_test)
    # for pred in pred_lr: 
    #     print(pred)

    ## Model 3 - SGD Regressor
    ml_sgd = SGDRegressor(shuffle=False, max_iter=10000, random_state=0, learning_rate='optimal')
    ml_sgd.fit(X_train, y_train)
    pred_sgd = ml_sgd.predict(X_test)
    for pred in pred_sgd: 
        print(pred)

    # ## Model 4 - Random Forest
    # ml_rf = RandomForestClassifier(n_estimators=10000, max_depth=20, random_state=0)
    # ml_rf.fit(X_train, y_train)
    # pred_rf = ml_rf.predict(X_test)
    # for pred in pred_rf: 
    #     print(pred)

    # ## Model 5 - Extra Trees (Extremely Random Forest)
    # ml_et = ExtraTreesClassifier()
    # ml_et.fit(X_train, y_train)
    # pred_et = ml_et.predict(X_test)
    # for pred in pred_et: 
    #     print(pred)


def main(): 
    df_train, df_test = read_data()
    model(df_train, df_test)


if __name__ == "__main__": 
    main()

