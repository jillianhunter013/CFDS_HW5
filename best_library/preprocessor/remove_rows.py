import pandas as pd


class RemoveNAPreprocessor:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def RemoveMissingVals(self) -> pd.DataFrame:
        
        """Removes rows with missing values in columns 'age', 'gender', or 'ethnicity'."""
        cleaned_df = self.dataframe.dropna(subset=['age', 'gender', 'ethnicity'])
        return cleaned_df