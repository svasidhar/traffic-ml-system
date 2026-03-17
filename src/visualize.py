import matplotlib.pyplot as plt

def plot_traffic_by_hour(df):
    avg = df.groupby('hour')['traffic_volume'].mean()

    plt.figure()
    plt.plot(avg)
    plt.title("Traffic Volume by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Traffic Volume")
    plt.show()


def plot_traffic_by_day(df):
    avg = df.groupby('day')['traffic_volume'].mean()

    plt.figure()
    plt.plot(avg)
    plt.title("Traffic Volume by Day")
    plt.xlabel("Day")
    plt.ylabel("Traffic Volume")
    plt.show()