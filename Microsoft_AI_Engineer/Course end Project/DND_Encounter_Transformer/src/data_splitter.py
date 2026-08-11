import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import RANDOM_STATE, SYNTHETIC_DATA_PATH, TEST_DATA_PATH, TEST_SIZE, TRAIN_DATA_PATH

df = pd.read_csv(SYNTHETIC_DATA_PATH)

def split_data(df, test_size=TEST_SIZE, random_state=RANDOM_STATE):
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    train_df.to_csv(TRAIN_DATA_PATH, index=False)
    test_df.to_csv(TEST_DATA_PATH, index=False)
    return train_df, test_df

# if __name__ == "__main__":
#     train_df, test_df = split_data(df)
#     print("Train/test split complete.")
#     print(f"Train rows: {len(train_df)}")
#     print(f"Test rows: {len(test_df)}")