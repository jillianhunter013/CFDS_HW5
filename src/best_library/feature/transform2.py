import pandas as pd
from ..base import BaseFeature

class AgeGroupFeature(BaseFeature):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def transform(self) -> pd.DataFrame:
        self.dataframe = self.dataframe.copy()
        if 'age' not in self.dataframe.columns:
            raise KeyError("Column 'age' required for AgeGroupFeature.")
        
        bins = [0, 18, 35, 50, 65, 120]
        labels = ['<18', '18-35', '35-50', '50-65', '65+']
        self.dataframe['age_group'] = pd.cut(self.dataframe['age'], bins=bins, labels=labels, right=False)
        return self.dataframe