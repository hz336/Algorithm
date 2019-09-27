# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import numpy as np

def read_data():
    num_obs = int(input())
    columns = [item for item in input().strip().split('\t')]
    num_cols = len(columns)
    df_array = [[np.nan for _ in range(num_cols)] for _ in range(num_obs)]
    for i in range(num_obs): 
        df_array[i][:] = [item for item in input().strip().split('\t')]
    df = pd.DataFrame(df_array, columns=columns)

    return df

def model(df): 
    df['tmax'] = df['tmax'].apply(lambda x: np.nan if x.startswith('Missing') else float(x))
    df['tmin'] = df['tmin'].apply(lambda x: np.nan if x.startswith('Missing') else float(x))
    df['tmax_ffill'] = df['tmax'].fillna(method='ffill')
    df['tmax_bfill'] = df['tmax'].fillna(method='bfill')
    df['tmin_ffill'] = df['tmin'].fillna(method='ffill')
    df['tmin_bfill'] = df['tmin'].fillna(method='bfill')

    for i in range(df.shape[0]): 
        for col in ['tmax', 'tmin']: 
            if pd.isnull(df.loc[i, col]): 
                avg = (df.loc[i, col + '_ffill']+ df.loc[i, col + '_bfill']) / 2
                print(avg)


def main(): 
    df = read_data()
    model(df)

if __name__ == '__main__': 
    main()
