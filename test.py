from src.preprocess import load_data, clean_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.visualize import plot_traffic_by_hour, plot_traffic_by_day

df = load_data("data/traffic.csv")
df = clean_data(df)

df = create_features(df)

model = train_model(df)

plot_traffic_by_hour(df)
plot_traffic_by_day(df)