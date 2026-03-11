import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/cleaned_data.csv")

st.title("Global Economic Intelligence Dashboard")

# Country selector
country = st.selectbox("Select Country", df["Country"].unique())

# Filter data
data = df[df["Country"] == country]
data = data.groupby("Year")["GDP_USD"].mean().reset_index()
data = data.sort_values("Year")

# Plot chart
fig, ax = plt.subplots()

ax.plot(data["Year"], data["GDP_USD"]/1e12, marker="o")

ax.set_title("GDP Trend - " + country)
ax.set_xlabel("Year")
ax.set_ylabel("GDP (Trillion USD)")

st.pyplot(fig)