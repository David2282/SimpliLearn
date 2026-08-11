from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def evaluate_model(model, X_train_reduced, y_train):
    train_predictions = model.predict(X_train_reduced)
    r2 = r2_score(y_train, train_predictions)
    rmse = mean_squared_error(y_train, train_predictions) ** 0.5
    mae = mean_absolute_error(y_train, train_predictions)

    print("Model Evaluation Metrics:")
    print(f"R2 Score: {r2}")
    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")