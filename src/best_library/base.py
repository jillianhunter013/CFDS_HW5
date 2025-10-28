from abc import ABC, abstractmethod
import pandas as pd

class BaseFeature(ABC):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def transform(self) -> pd.DataFrame:
        pass
