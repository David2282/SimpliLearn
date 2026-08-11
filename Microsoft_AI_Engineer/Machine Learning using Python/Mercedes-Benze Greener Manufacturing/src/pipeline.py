from src.data_loader import load_data
from src.predictor import make_predictions
from src.preprocessor import preprocess_data
from src.model_trainer import train_model
from src.evaluator import evaluate_model


def run_pipeline():
    train_df, test_df = load_data()

    X_train, y_train, X_test = preprocess_data(train_df, test_df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_train, y_train)
    predictions = make_predictions(model, X_test)

    print("Processed train shape:", X_train.shape)
    print("Target shape:", y_train.shape)
    print("Processed test shape:", X_test.shape)
    print("Preprocessing completed successfully!")

    # X_train_reduced, y_train, X_test_reduced = preprocess_data(train_df, test_df)

    # model = train_model(X_train_reduced, y_train)
    # predictions = make_predictions(model, X_test_reduced)
    #evaluate_model(model, X_train_reduced, y_train)

    # print("Processed train shape:", X_train_reduced.shape)
    # print("Target shape:", y_train.shape)
    # print("Processed test shape:", X_test_reduced.shape)
    # print("Preprocessing completed successfully!")
    
    
    print(predictions[:5])  # Print first 5 predictions

if __name__ == "__main__":
    run_pipeline()