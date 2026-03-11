import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")

country = "India"

data = df[df["Country"].str.strip() == country]

print(data.head())

plt.figure()

plt.plot(data["Year"], data["GDP_USD"])

plt.title("GDP Trend - " + country)
plt.xlabel("Year")
plt.ylabel("GDP")

plt.show()