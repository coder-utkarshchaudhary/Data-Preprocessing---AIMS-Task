import pandas as pd
import numpy as np

class SimpleImputer:
    def __init__(self, strategy, fill_value):
        strategyList = ['mean', 'median', 'most_frequent', 'constant']

        if strategy not in strategyList:
            raise Exception("Invalid Strategy")
        
        self.strategy = strategy
        self.fill_value = fill_value

        if self.strategy == 'constant':
            if self.fill_value == None:
                self.fill_value = 0
            else:
                self.fill_value = fill_value
        
    def impute(self, dataframe, columns):
        self.df = dataframe

        for col in columns:
            if self.strategy == 'mean':
                self.df[col] = self.df[col].fillna(self.df[col].mean())
            elif self.strategy == 'median':
                self.df[col] = self.df[col].fillna(self.df[col].median())
            elif self.strategy == 'most_frequent':
                self.df[col] = self.df[col].fillna(self.df[col].mode())
            else:
                self.df[col] = self.df[col].fillna(self.fill_value)

        return self.df

if __name__ == '__main__':
    # path = "" # Path to the csv file
    # df = pd.read_csv(path)
    array = np.array([2,3,5,6,7,np.nan,8,101,324,np.nan,32,np.nan,np.nan])
    # array = array.transpose

    df = pd.DataFrame(array)

    imputerInstance = SimpleImputer('mean', None)
    df = imputerInstance.impute(df, df.columns)
    print(df)