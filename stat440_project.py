import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#read the dataset
df = pd.read_csv("2012-sat-results.csv")

print(df.info())
print("")

# convert all values to numeric
df["SAT Critical Reading Avg. Score"] = pd.to_numeric(df["SAT Critical Reading Avg. Score"], errors="coerce")
df["SAT Math Avg. Score"] = pd.to_numeric(df["SAT Math Avg. Score"], errors="coerce")
df["SAT Writing Avg. Score"] = pd.to_numeric(df["SAT Writing Avg. Score"], errors="coerce")

# Drop rows with NaN values
df = df.dropna(subset=["SAT Critical Reading Avg. Score", "SAT Math Avg. Score", "SAT Writing Avg. Score"])

print(df.info())
print("")

# population params
mu = df["SAT Writing Avg. Score"].mean()
tao = df["SAT Writing Avg. Score"].sum()
sigmasq = df["SAT Writing Avg. Score"].var(ddof=0)

print(df["SAT Writing Avg. Score"].max())
print(df["SAT Writing Avg. Score"].min())


print(f"The mu is: {mu}")
print(f"The tao is: {tao}")
print(f"The sigma^2 is: {sigmasq}")

print("")

plt.hist(df["SAT Writing Avg. Score"], bins=15, color="skyblue", alpha=0.8, edgecolor="black")
plt.title("SAT Writing Avg. Score NYC Schools")
plt.xlabel("Avg Writing Score")
plt.show()
