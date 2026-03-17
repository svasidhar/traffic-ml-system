from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import pandas as pd   # ✅ THIS LINE (IMPORTANT)

def train_model(df):
    print("Starting Model Training...")

    df = pd.get_dummies(df, columns=['weather_main', 'holiday'], drop_first=True)

    X = df.drop(['traffic_volume', 'date_time', 'weather_description'], axis=1)
    y = df['traffic_volume']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Training Completed")
    print("MAE:", mae)
    print("R2 Score:", r2)

    # Save model
    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    # Save columns
    with open('models/columns.pkl', 'wb') as f:
        pickle.dump(X.columns.tolist(), f)

    return model