import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

st.title("🌸 Iris Dataset Explorer")

feature = st.selectbox("Choose a feature to visualize:", iris.feature_names)
species_filter = st.multiselect("Filter by species:", iris.target_names, default=iris.target_names)

filtered_df = df[df['species'].isin(species_filter)]

fig, ax = plt.subplots()
for species in species_filter:
    subset = filtered_df[filtered_df['species'] == species]
    ax.hist(subset[feature], bins=10, alpha=0.5, label=species)

ax.set_xlabel(feature)
ax.set_ylabel("Count")
ax.set_title(f"Distribution of {feature}")
ax.legend()

st.pyplot(fig)
