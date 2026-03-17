import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Data Loaded Successfully")
    print(df.head())
    return df

def clean_data(df):
    print("Cleaning Data...")

    # Convert to datetime
    df['date_time'] = pd.to_datetime(df['date_time'])

    # Fill missing values
    df['temp'] = df['temp'].fillna(df['temp'].mean())
    df['rain_1h'] = df['rain_1h'].fillna(0)
    df['snow_1h'] = df['snow_1h'].fillna(0)
    df['clouds_all'] = df['clouds_all'].fillna(df['clouds_all'].median())
    df['weather_main'] = df['weather_main'].fillna(df['weather_main'].mode()[0])
    df['holiday'] = df['holiday'].fillna('None')

    # ✅ THIS LINE MUST BE SAME ALIGNMENT
    df = df.drop_duplicates()

    # Remove invalid values
    df = df[df['traffic_volume'] > 0]

    print("Data Cleaning Completed")
    return df