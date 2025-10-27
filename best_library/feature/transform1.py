import pandas as pd
from base import BaseFeature

class BMIFeature(BaseFeature):

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if {'weight', 'height'}.issubset(df.columns):
            df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
        else:
            raise KeyError("Columns 'weight' and 'height' required for BMIFeature.")
        return df
