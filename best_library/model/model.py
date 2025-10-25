
class Model():
    def __init__(self, columns: list[int], target: list[int], hyperparameters: dict):
        self._columns = columns
        self._target = target
        self._hyperparameters = hyperparameters
        self.model = LogisticRegression(hyperparameters)
    
    def train(self, training_data_X, training_data_y):
        self.model.fit(training_data_X, training_data_y)


    def predict(self, df: pd.DataFrame) -> list[int]:
        data_X = df.iloc[:, self._columns]
        predictions = self.model.predict(data_X)
        return predict_

import pandas as pd
from sklearn.linear_model import LogisticRegression
from typing import List, Optional, Type
import numpy as np


class Model():
    def __init__(self, features: List[str], target: str, params: Optional[dict] = None):
    
        self._features = features
        self._target = target
        self._params = params or {}
        self.model = LogisticRegression(**self._params)

    def train(self, df: pd.DataFrame):

        missing_features = [f for f in self._features if f not in df.columns]
        if missing_features:
            raise ValueError(f"Missing feature columns: {missing_features}")

        if self._target not in df.columns:
            raise ValueError(f"Target column '{self._target}' not found in DataFrame")

        
        X = df[self._features]
        y = df[self._target]

        self.model.fit(X, y)

    def predict(self, df: pd.DataFrame):

        missing_features = [f for f in self._features if f not in df.columns]
        if missing_features:
            raise ValueError(f"Missing feature columns: {missing_features}")

        X = df[self._features]

        return  self.model.predict_proba(X)[:, 1]
