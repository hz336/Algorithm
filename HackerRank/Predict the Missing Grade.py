# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import json 
import numpy as np 
from sklearn import tree
from numpy import nanmean

full_list = ['English', 'Physics', 'Chemistry', 'ComputerScience', 'Biology', 'PhysicalEducation', 'Economics', 'Accountancy', 'BusinessStudies', 'Mathematics']

def read_train_data():
    f = open('training.json', 'r')
    lines = f.readlines()
    f.close()
    
    N = int(lines[0].strip())
    all_X = np.array([[np.nan for j in range(len(full_list))] for i in range(N)])
    
    for i in range(N):
        df = json.loads(lines[i + 1])
        for item in full_list:
            j = full_list.index(item)
            if item in df.keys():
                all_X[i][j] = int(df[item])
    
    all_X = fill_missing(all_X)

    X = all_X[:, 0:len(full_list)-1]
    Y = all_X[:, len(full_list)-1]
    
    return X, Y
    
def read_test_data():
    N = int(input().strip())    
    test_X = [[np.nan for j in range(len(full_list)-1)] for i in range(N)]
    for i in range(N):
        df = json.loads(input())
        for item in full_list:
            if item != 'Mathematics' and item in df.keys():
                j = full_list.index(item)
                test_X[i][j] = df[item] 
    test_X = fill_missing(test_X)
    return test_X

def fill_missing(X_in):
    mean = nanmean(X_in, axis=0)
    for rows in range(len(X_in)):
        for cols in range(len(X_in[rows])):
            if np.isnan(X_in[rows][cols]):
                X_in[rows][cols] = int(mean[cols])
    return X_in
    
if __name__ == "__main__":
    
    train_X, train_Y = read_train_data()
    clf = tree.DecisionTreeClassifier() 
    clf = clf.fit(train_X, train_Y)
    
    test_X = read_test_data()

    pred = clf.predict(test_X)
    for item in pred:
        print(int(item))
  