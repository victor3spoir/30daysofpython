###day-25
# exercice
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1
df = pd.read_csv(Path("./data/hacker_news.csv").resolve().as_posix())

# 2
head_rows = df.head(5)
print(head_rows)

# 3
tail_rows = df.tail(5)
print(tail_rows)

# 4
print("rows", df.shape[0])
print("columns", df.shape[1])

# 5
title_contains_python_df = df[df["title"].str.contains("python", case=False, na=False)]
print(title_contains_python_df.loc[:, "title"].to_list())

title_contains_js_df = df[df["title"].str.contains("JavaScript", case=False, na=False)]
print(title_contains_js_df.loc[:, "title"].to_list())

# some analysis
print(df.info())
print(df.describe())

top_rated = df.sort_values(by="num_points", ascending=False).head(5)
print(top_rated.loc[:, ["title"]])
top_commented = df.sort_values(by="num_comments", ascending=False).head(5)
print(top_commented)
top_authors = df["author"].value_counts().head(5)
print(top_authors)


#
fig, ax = plt.subplots(figsize=(8, 6))


ax.scatter(df["num_points"], df["num_comments"], color="blue", alpha=0.7)

ax.set_xlabel("Points")
ax.set_ylabel("Comments")
ax.set_title("Engagement: Points vs Comments")

fig.tight_layout()
plt.show()
