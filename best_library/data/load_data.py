import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath: str) -> pd.DataFrame:
    """Load the dataset from CSV."""
    return pd.read_csv(filepath)


def split_data(df: pd.DataFrame, test_size=0.2, random_state=42):
    """Split dataset into train and test sets."""
    return train_test_split(df, test_size=test_size, random_state=random_state)


class LoadData:
    """Class to load and split data from a given filepath."""

    """Initialize with the filepath to the dataset."""
    def __init__(self, filepath: str):
        self.filepath = filepath

    """Function that loads and splits the data into training and testing sets."""
    def load_and_split(self, test_size=0.2, random_state=42):
        df = load_data(self.filepath)
        train_df, test_df = split_data(df, test_size=test_size, random_state=random_state)
        return train_df, test_df