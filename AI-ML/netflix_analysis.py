import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

df.drop_duplicates(subset="show_id", inplace=True)

df["country"] = df["country"].fillna("Unknown")
df["director"] = df["director"].fillna("Not Available")


df["Is_Recent"] = df["release_year"].apply(lambda x: 1 if x >= 2015 else 0)

df["duration_minutes"] = pd.NA
df["seasons"] = pd.NA

df.loc[df["type"] == "Movie", "duration_minutes"] = (
    df.loc[df["type"] == "Movie", "duration"]
    .str.replace(" min", "", regex=False)
)

df.loc[df["type"] == "TV Show", "seasons"] = (
    df.loc[df["type"] == "TV Show", "duration"]
    .str.replace(" Seasons", "", regex=False)
    .str.replace(" Season", "", regex=False)
)

df["duration_minutes"] = pd.to_numeric(df["duration_minutes"], errors="coerce")
df["seasons"] = pd.to_numeric(df["seasons"], errors="coerce")


