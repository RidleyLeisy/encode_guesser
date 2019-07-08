import pandas as pd
import category_encoders as ce
from sklearn.pipeline import make_pipeline

class EncodeGuesser():
    def __init__(self, DataFrame):
        self.df = DataFrame
        return

    def guess(self, threshold=50):
        df = self.df
        cats = df.describe(exclude='number').T[['unique']]
        binary_cols = list(cats.loc[cats['unique'] > threshold].index)
        one_hot_cols = list(cats.loc[cats['unique'] <= threshold].index)
        self.binary_cols = binary_cols
        self.one_hot_cols = one_hot_cols

        if len(binary_cols) == 0:
            message = f'''Since all of your columns have low cardinality, we are
            suggesting you use One Hot Encoding for columns: {one_hot_cols}. '''
            
            
        else:
            message = f'''Due to the high cardinality of columns: {binary_cols}. We are
            suggesting you use binary encoding. For the lower cardinality columns: {one_hot_cols}. 
            We suggest using one hot encoding.'''
        
        print(message)
        
        return self.__make_pipeline(self)


    @staticmethod
    def __make_pipeline(self):

        txt = input('Do you wish to create a pipeline with our suggestion (Y/n)?')
        if txt.upper() == 'Y':
            pipeline = make_pipeline(ce.BinaryEncoder(cols=self.binary_cols),
                        ce.OneHotEncoder(cols=self.one_hot_cols))
            return pipeline
        else:
            return print('Ok, we will not return a pipeline.')
         
