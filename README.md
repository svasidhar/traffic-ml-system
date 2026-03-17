# 🚦 Urban Traffic Congestion Intelligence System

## 📌 Overview

Urban traffic congestion is a major challenge in modern cities, leading to delays, fuel wastage, and pollution.
This project presents an **AI-powered traffic prediction system** that analyzes historical traffic and environmental data to predict congestion levels in real time.

The system uses **Machine Learning (Random Forest)** to provide accurate traffic insights and an interactive dashboard built with **Streamlit**.

---

## 🚀 Features

* 📊 Traffic Pattern Analysis (Day-wise trends)
* 🔥 Congestion Heatmap (Hour vs Day)
* 🌦 Weather Impact Analysis on traffic
* 📉 Weekday vs Weekend comparison
* 🤖 AI-based Traffic Prediction System
* 🚦 Traffic Risk Classification (Low / Moderate / Heavy)
* 🎯 Interactive Dashboard for visualization

---

## 🧠 Machine Learning Model

* Model Used: **Random Forest Regressor**
* Why Random Forest?

  * Handles non-linear relationships
  * High accuracy and robustness
  * Works well with real-world noisy data

### 📈 Performance

* R² Score: ~0.95
* MAE: ~244

---

## 🗂 Project Structure

```
traffic_project/
│
├── data/
│   └── traffic.csv
│
├── models/           # Generated after training
│   ├── model.pkl
│   └── columns.pkl
│
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── visualize.py
│
├── app.py            # Streamlit Dashboard
├── test.py           # Model training script
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/svasidhar/traffic-ml-system.git
cd traffic-ml-system
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Train Model (IMPORTANT)

```
python test.py
```

👉 This will create:

* `models/model.pkl`
* `models/columns.pkl`

---

### 4️⃣ Run Application

```
streamlit run app.py
```

---

## 🖥️ Dashboard Modules

### 📊 Dashboard

* Traffic trends across days

### 🔥 Heatmap

* Congestion visualization by hour & day

### 🌦 Weather Analysis

* Impact of weather conditions on traffic

### 📉 Weekday vs Weekend

* Comparative traffic behavior

### 🚦 Prediction

* Input:

  * Hour
  * Day
  * Month
  * Temperature
* Output:

  * Traffic volume
  * Congestion level

---

## 🎯 Use Cases

* Smart City Traffic Management
* Route Optimization Systems
* Urban Planning & Infrastructure
* Emergency Vehicle Routing
* Pollution Reduction Strategies

---

## 🔮 Future Enhancements

* 📡 Real-time traffic data integration (IoT)
* 🗺 Google Maps API integration
* 📱 Mobile app deployment
* 🚦 Smart signal automation
* 📊 Deep Learning models for improved accuracy

---

## 👨‍💻 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit

---

## ⚠️ Note

The trained model is **not included** due to size limitations.

👉 Run:

```
python test.py
```

to generate the model before launching the app.

---

## 🏆 Conclusion

This project demonstrates how **AI and data-driven insights** can transform urban traffic systems, making cities smarter, more efficient, and sustainable.

---

## 📌 Author

Code Forces Team
---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---
