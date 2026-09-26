import pandas as pd
import numpy as np


INPUT_FILE = "titles.csv"


OUTPUT_FILE = "cleaned_titles.csv"


df = pd.read_csv(INPUT_FILE)

print("========== ORIGINAL DATA ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== COLUMNS ==========")
print(df.columns.tolist())


print("\n========== MISSING VALUES BEFORE ==========")
print(df.isnull().sum())


print("\nDuplicate rows:", df.duplicated().sum())


df = df.drop_duplicates()

# Remove leading/trailing spaces from text columns
text_columns = [
    "title",
    "type",
    "description",
    "age_certification",
    "genres",
    "production_countries"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

# Convert numeric columns
numeric_columns = [
    "release_year",
    "runtime",
    "seasons",
    "imdb_score",
    "imdb_votes",
    "tmdb_popularity",
    "tmdb_score"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove impossible values
df.loc[df["release_year"] < 1900, "release_year"] = np.nan
df.loc[df["runtime"] < 0, "runtime"] = np.nan
df.loc[df["seasons"] < 0, "seasons"] = np.nan
df.loc[df["imdb_score"] < 0, "imdb_score"] = np.nan
df.loc[df["tmdb_score"] < 0, "tmdb_score"] = np.nan

# Fill missing text values
df["description"] = df["description"].fillna("Unknown")
df["age_certification"] = df["age_certification"].fillna("Not Rated")
df["imdb_id"] = df["imdb_id"].fillna("Unknown")


numeric_fill_columns = [
    "imdb_score",
    "imdb_votes",
    "tmdb_popularity",
    "tmdb_score"
]

for col in numeric_fill_columns:
    df[col] = df[col].fillna(df[col].median())


df.to_csv(OUTPUT_FILE, index=False)

print("\n========== CLEANING COMPLETE ==========")
print("Rows after cleaning:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== MISSING VALUES AFTER ==========")
print(df.isnull().sum())

print("\nCleaned file saved as:", OUTPUT_FILE)