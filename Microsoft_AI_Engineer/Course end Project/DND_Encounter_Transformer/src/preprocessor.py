from src.config import TRAIN_DATA_PATH, TEST_DATA_PATH
import pandas as pd

def load_data(train_path=TRAIN_DATA_PATH, test_path=TEST_DATA_PATH):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def preprocess_data(train_df, test_df):
    feasibility_label_mapping = {"Possible": 1, "Not Possible": 0}
    X_train = train_df["encounter_description"]
    y_train = train_df["feasibility_label"].map({
        "Possible": 1,
        "Not Possible": 0   
        })
    X_test = test_df["encounter_description"]
    y_test = test_df["feasibility_label"].map({
        "Possible": 1,
        "Not Possible": 0   
        })
    return X_train, y_train, X_test, y_test