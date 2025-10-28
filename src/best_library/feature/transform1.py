import pandas as pd
from ..base import BaseFeature

class BMIFeature(BaseFeature):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def transform(self) -> pd.DataFrame:
        self.dataframe = self.dataframe.copy()
        if {'weight', 'height'}.issubset(self.dataframe.columns):
            self.dataframe['bmi'] = self.dataframe['weight'] / ((self.dataframe['height'] / 100) ** 2)
        else:
            raise KeyError("Columns 'weight' and 'height' required for BMIFeature.")
        return self.dataframe
