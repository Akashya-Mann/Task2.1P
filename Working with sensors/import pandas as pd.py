import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("hc_sr04_data.csv", names=["timestamp", "distance"])
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y%m%d%H%M%S")
df["distance"] = pd.to_numeric(df["distance"], errors='coerce')
df.dropna(inplace=True)
plt.plot(df["timestamp"], df["distance"], color="blue")
plt.title("Motion Data - Distance / Time ")
plt.xlabel("Timestamps")
plt.ylabel("Distance(cm)")
plt.grid(True)
plt.tight_layout()
plt.show()
