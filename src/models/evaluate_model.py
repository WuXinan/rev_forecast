from sklearn.metrics import mean_absolute_error

def evaluate_model(y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    print(f'MAE: {mae}')
