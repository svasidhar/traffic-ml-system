import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Traffic AI System",
    page_icon="🚦",
    layout="wide"
)

# -------------------- STYLE --------------------
st.markdown("""
<style>
.main { background-color: #0E1117; }
h1, h2, h3 { color: #FFFFFF; }
.stButton>button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.title("Traffic Intelligence Dashboard")
st.markdown("### AI-Powered Traffic Prediction & Analysis Platform")
st.markdown("---")

# -------------------- LOAD MODEL --------------------
model = pickle.load(open('models/model.pkl', 'rb'))
columns = pickle.load(open('models/columns.pkl', 'rb'))

# -------------------- LOAD DATA --------------------
df = pd.read_csv('data/traffic.csv')
df['date_time'] = pd.to_datetime(df['date_time'])
df['hour'] = df['date_time'].dt.hour
df['day'] = df['date_time'].dt.dayofweek

# -------------------- SIDEBAR NAVIGATION --------------------
page = st.sidebar.radio("📌 Navigation", [
    "Dashboard",
    "Heatmap",
    "Weather Analysis",
    "Weekday vs Weekend",
    "Prediction"
])

# -------------------- DASHBOARD --------------------
if page == "Dashboard":

    st.header("Traffic Pattern Insights")

    col1, col2 = st.columns(2)

    # Traffic by Day
    with col1:
        fig1, ax1 = plt.subplots(figsize=(5,3))
        df.groupby('day')['traffic_volume'].mean().plot(ax=ax1)
        ax1.set_title("Traffic by Day")
        st.pyplot(fig1)

    # Traffic by Hour
    with col2:
        fig2, ax2 = plt.subplots(figsize=(5,3))
        df.groupby('hour')['traffic_volume'].mean().plot(ax=ax2)
        ax2.set_title("Traffic by Hour")
        st.pyplot(fig2)

# -------------------- HEATMAP --------------------
elif page == "Heatmap":

    st.header("Traffic Congestion Heatmap")

    pivot = df.pivot_table(values='traffic_volume', index='day', columns='hour')

    fig, ax = plt.subplots()
    sns.heatmap(pivot, cmap='coolwarm', ax=ax)
    ax.set_title("Traffic Heatmap (Day vs Hour)")

    st.pyplot(fig)

# -------------------- WEATHER ANALYSIS --------------------
elif page == "Weather Analysis":

    st.header("Weather Impact on Traffic")

    fig, ax = plt.subplots()
    df.groupby('weather_main')['traffic_volume'].mean().plot(kind='bar', ax=ax)
    ax.set_title("Traffic by Weather Condition")
    plt.xticks(rotation=45)

    st.pyplot(fig)

# -------------------- WEEKDAY VS WEEKEND --------------------
elif page == "Weekday vs Weekend":

    st.header("Weekday vs Weekend Analysis")

    df['type'] = df['day'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

    fig, ax = plt.subplots()
    df.groupby('type')['traffic_volume'].mean().plot(kind='bar', ax=ax)
    ax.set_title("Weekday vs Weekend Traffic")

    st.pyplot(fig)

# -------------------- PREDICTION --------------------
elif page == "Prediction":

    st.header("Traffic Prediction")

    hour = st.slider("Hour of Day", 0, 23)
    day = st.slider("Day (0=Mon, 6=Sun)", 0, 6)
    month = st.slider("Month", 1, 12)
    temp = st.number_input("Temperature (Kelvin)", value=300.0)

    st.markdown("## Predict Traffic")

    if st.button("Predict Traffic"):

        data = pd.DataFrame(columns=columns)
        data.loc[0] = 0

        data['hour'] = hour
        data['day'] = day
        data['month'] = month
        data['temp'] = temp
        data['is_weekend'] = 1 if day >= 5 else 0
        data['is_peak_hour'] = 1 if (7 <= hour <= 9 or 16 <= hour <= 18) else 0

        prediction = model.predict(data)
        traffic = int(prediction[0])

        st.subheader("Prediction Result & Risk Level")

        if traffic < 2000:
            st.success(f"🟢 Low Traffic: {traffic}")
            st.info("Smooth traffic flow. Ideal for travel 🚗")
        elif traffic < 4000:
            st.warning(f"🟡 Moderate Traffic: {traffic}")
            st.info("Moderate congestion. Expect slight delays ⏳")
        else:
            st.error(f"🔴 Heavy Traffic: {traffic}")
            st.info("High congestion detected. Consider alternative routes 🚧")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("👨‍💻 Developed for Code_Forces | AI Traffic Intelligence System")