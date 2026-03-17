import pandas as pd

def create_features(df):
    print("Starting Feature Engineering...")

    df['hour'] = df['date_time'].dt.hour
    df['day'] = df['date_time'].dt.dayofweek
    df['month'] = df['date_time'].dt.month

    df['is_weekend'] = df['day'].apply(lambda x: 1 if x >= 5 else 0)
    df['is_peak_hour'] = df['hour'].apply(lambda x: 1 if (7 <= x <= 9 or 16 <= x <= 18) else 0)

    # ✅ ADD HERE (IMPORTANT)
    df['rush_hour'] = df['hour'].apply(lambda x: 
        'morning' if 7 <= x <= 10 else 
        'evening' if 16 <= x <= 19 else 
        'off_peak')

    df = pd.get_dummies(df, columns=['rush_hour'], drop_first=True)

    print("Feature Engineering Completed")
    return df