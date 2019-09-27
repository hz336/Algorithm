# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def read_data(): 
    ## training set
    num_fea, num_train = input().strip().split(' ')
    num_fea = int(num_fea)
    num_train = int(num_train)

    df_array = [[np.nan for _ in range(num_fea + 1)] for _ in range(num_train)]
    for i in range(num_train): 
        df_array[i][:] = [item for item in input().strip().split(' ')]
    
    columns = ['feature_%s' % i for i in range(1, num_fea + 1)]
    columns.append('price')
    df_train = pd.DataFrame(df_array, columns=columns)
    df_train = df_train.astype(float)
    
    ## test set
    num_test = input().strip()
    num_test = int(num_test)
    
    df_array = [[np.nan for _ in range(num_fea)] for _ in range(num_test)]
    for i in range(num_test): 
        df_array[i][:] = [item for item in input().strip().split(' ')]
    
    columns = ['feature_%s' % i for i in range(1, num_fea + 1)]
    df_test = pd.DataFrame(df_array, columns=columns)
    df_test = df_test.astype(float)

    return num_fea, df_train, df_test


def model(num_fea, df_train, df_test): 
    df_train, df_val = train_test_split(df_train, test_size=0.05, shuffle=False, random_state=0)
    X_train, y_train = df_train.iloc[:, df_train.columns!='price'].values, df_train['price'].values
    X_test = df_test.iloc[:, df_test.columns!='price'].values

    model_lr = LinearRegression()
    model_lr.fit(X_train, y_train)
    pred_lr = model_lr.predict(X_test)
    for pred in pred_lr: 
        print(pred)


def main(): 
    num_fea, df_train, df_test = read_data()
    model(num_fea, df_train, df_test)


if __name__ == '__main__': 
    main()

