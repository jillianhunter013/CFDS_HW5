import pandas as pd
from .base_feature import BaseFeature

class AgeGroupFeature(BaseFeature):

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if 'age' not in df.columns:
            raise KeyError("Column 'age' required for AgeGroupFeature.")
        
        bins = [0, 18, 35, 50, 65, 120]
        labels = ['<18', '18-35', '35-50', '50-65', '65+']
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
        return df
