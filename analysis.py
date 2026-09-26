import pandas as pd
import matplotlib.pyplot as plt
import os


INPUT_FILE = "cleaned_titles.csv"

df = pd.read_csv(INPUT_FILE)


os.makedirs("graphs", exist_ok=True)

print("========== OTT CONTENT ANALYSIS ==========")

# ==============================
# BASIC INFORMATION
# ==============================

print("\nTotal Titles:", len(df))

print("\nContent Type:")
print(df["type"].value_counts())

print("\nAverage IMDb Score:",
      round(df["imdb_score"].mean(), 2))


# ==============================
# 1. MOVIES VS TV SHOWS
# ==============================

type_count = df["type"].value_counts()

plt.figure(figsize=(7, 5))
type_count.plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("graphs/movies_vs_tv_shows.png")
plt.show()


# ==============================
# 2. CONTENT BY RELEASE YEAR
# ==============================

year_count = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(year_count.index, year_count.values)

plt.title("Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()

plt.savefig("graphs/content_by_year.png")
plt.show()


# ==============================
# 3. TOP GENRES
# ==============================

genre_data = (
    df["genres"]
    .dropna()
    .astype(str)
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genre_data.value_counts().head(10)

print("\nTop 10 Genres:")
print(top_genres)

plt.figure(figsize=(9, 5))
top_genres.sort_values().plot(kind="barh")

plt.title("Top 10 Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()

plt.savefig("graphs/top_genres.png")
plt.show()


# ==============================
# 4. TOP COUNTRIES
# ==============================

country_data = (
    df["production_countries"]
    .dropna()
    .astype(str)
    .str.split(",")
    .explode()
    .str.strip()
)

top_countries = country_data.value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

plt.figure(figsize=(9, 5))
top_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig("graphs/top_countries.png")
plt.show()


# ==============================
# 5. IMDb SCORE DISTRIBUTION
# ==============================

plt.figure(figsize=(8, 5))

plt.hist(
    df["imdb_score"].dropna(),
    bins=10,
    edgecolor="black"
)

plt.title("IMDb Score Distribution")
plt.xlabel("IMDb Score")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig("graphs/imdb_score_distribution.png")
plt.show()


# ==============================
# 6. RUNTIME ANALYSIS
# ==============================

runtime_data = df["runtime"].dropna()

plt.figure(figsize=(8, 5))

plt.hist(
    runtime_data,
    bins=20,
    edgecolor="black"
)

plt.title("Runtime Distribution")
plt.xlabel("Runtime (Minutes)")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig("graphs/runtime_distribution.png")
plt.show()


# ==============================
# FINAL SUMMARY
# ==============================

print("\n========== SUMMARY ==========")

print("Total Titles:", len(df))

print("Movies:", (df["type"] == "MOVIE").sum())

print("TV Shows:", (df["type"] == "SHOW").sum())

print("Average IMDb Score:",
      round(df["imdb_score"].mean(), 2))

print("Average Runtime:",
      round(df["runtime"].mean(), 2), "minutes")

print("\nAll graphs saved inside the 'graphs' folder.")