import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

from src.config import TARGET_COLUMN

def preprocess_data(train_df, test_df):
    y_train = train_df[TARGET_COLUMN]
    X_train = train_df.drop(columns=[TARGET_COLUMN]).copy()
    X_test = test_df.copy()

    # null + unique checks
    print("Train nulls:\n", X_train.isnull().sum().sum())
    print("Test nulls:\n", X_test.isnull().sum().sum())

    print("Train unique values:\n", X_train.nunique())
    print("Test unique values:\n", X_test.nunique())

    # remove zero variance cols
    zero_var_cols = [col for col in X_train.columns if X_train[col].nunique() == 1]
    X_train = X_train.drop(columns=zero_var_cols)
    X_test = X_test.drop(columns=zero_var_cols)

    print("Removed zero variance columns:", zero_var_cols)

    # label encode object cols
    categorical_cols = X_train.select_dtypes(include=['object']).columns

    for col in categorical_cols:
        le = LabelEncoder()
        combined = list(X_train[col].astype(str)) + list(X_test[col].astype(str))
        le.fit(combined)
        X_train[col] = le.transform(X_train[col].astype(str))
        X_test[col] = le.transform(X_test[col].astype(str))

    # print("Shape before PCA:", X_train.shape)
    # PCA
    # pca = PCA(n_components=0.95, random_state=42)  # Adjust as needed
    # X_train_reduced = pca.fit_transform(X_train)
    # X_test_reduced = pca.transform(X_test)

    #print("Shape after PCA:", X_train_reduced.shape)

    print("Original train shape:", X_train.shape)
    # print("Reduced train shape:", X_train_reduced.shape)
    # print("Reduced test shape:", X_test_reduced.shape)

    return X_train, y_train, X_test  # X_train_reduced, y_train, X_test_reduced