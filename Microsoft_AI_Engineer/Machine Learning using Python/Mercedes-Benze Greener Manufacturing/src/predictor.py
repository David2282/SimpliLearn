def make_predictions(model, X_test):
    predictions = model.predict(X_test)
    return predictions
    print("Predictor input shape:", X_test.shape)