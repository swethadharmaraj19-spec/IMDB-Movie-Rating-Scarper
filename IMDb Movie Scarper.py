import pandas as pd

# Load files
basics = pd.read_csv(
    "title.basics.tsv.gz",
    sep="\t",
    low_memory=False
)

ratings = pd.read_csv(
    "title.ratings.tsv.gz",
    sep="\t"
)

# Movies மட்டும்
movies = basics[
    (basics["titleType"] == "movie") &
    (basics["startYear"] != "\\N")
]

# Ratings join
df = movies.merge(ratings, on="tconst")

# Votes அடிப்படையில் sort
top250 = df.sort_values(
    by="numVotes",
    ascending=False
).head(250)

# Required columns
result = top250[
    ["primaryTitle", "startYear", "averageRating", "numVotes"]
]

result.columns = [
    "Movie Name",
    "Year",
    "Rating",
    "Votes"
]

# Save CSV
result.to_csv(
    "imdb_top_250_movies.csv",
    index=False
)

print(result.head())
print("250 movies saved successfully!")