import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../data/cleaned_data.csv")
data = df[df["Country"] == "India"]
data = data.groupby("Year")["GDP_USD"].mean().reset_index()
data = data.sort_values("Year")
plt.figure()
plt.plot(data["Year"], data["GDP_USD"]/1e12, marker="o")
plt.title("GDP Trend - India")
plt.xlabel("Year")
plt.ylabel("GDP (Trillion USD)")
plt.grid(True)
plt.show()