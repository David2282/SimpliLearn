import pandas as pd

from src.config import TEST_PATH, TRAIN_PATH

def load_data():
    # read train.csv
    train_df = pd.read_csv(TRAIN_PATH)
    # read test.csv
    test_df = pd.read_csv(TEST_PATH)
    return train_df, test_df



