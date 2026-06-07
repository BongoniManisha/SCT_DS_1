import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_282912.csv", skiprows=4)
data = df[["Country Name", "2022"]].dropna()
data = data[data["2022"] > 0]
top10 = data.sort_values("2022", ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(top10["Country Name"], top10["2022"])
plt.xlabel("Countries")
plt.ylabel("Population in 2022")
plt.title("Top 10 Countries by Population in 2022")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()