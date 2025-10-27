import pandas as pd

class FillNaNPreprocessor:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def FillMissingVals(self) -> pd.DataFrame:
        
        """Fills NaN values in columns 'height' and 'weight' with the mean of the respective columns."""
        for column in ['height', 'weight']:
            if column in self.dataframe.columns:
                mean_value = self.dataframe[column].mean()
                self.dataframe[column].fillna(mean_value, inplace=True)
        return self.dataframe
