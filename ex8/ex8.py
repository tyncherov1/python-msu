import matplotlib.pyplot as plt
import pandas as pd

min_count = 30

df = pd.read_csv(
    r"data\anime-dataset-2023.csv",
    na_values=["UNKNOWN"],
    usecols=["Name", "Score"],
).dropna()

df["Score"] = df["Score"].astype(float)
df["words"] = (
    df["Name"]
    .astype(str)
    .str.lower()
    .str.findall(r"[a-z0-9.]+")
    .map(set)
)

###########################################################################################
stats_tb = (
    df.explode("words")
    .groupby("words", as_index=False)["Score"]
    .agg(n="count", k="mean")
)

result_tb = (
    stats_tb[stats_tb['n'] >= min_count]
    .sort_values(["k", 'n'], ascending=False)
    .reset_index(drop=True)
)

top20_tb = result_tb.head(20)[::-1]

plt.figure(figsize=(6, 4))
plt.barh(top20_tb["words"], top20_tb["k"])
plt.xlabel("Средний Score")
plt.ylabel("Слово")
plt.title("Топ-20 слов по среднему Score")
plt.tight_layout()

#########################################################################################################################
threshold = df["Score"].quantile(0.75)
df["is_high"] = (df["Score"] >= threshold).astype(int)
p_base = df["is_high"].mean()

stats = (
    df.explode("words")
    .groupby("words")["is_high"]
    .agg(n="count", k="sum")
)

m = 20.0
stats["smooth_rate"] = (stats["k"] + m * p_base) / (stats["n"] + m)
stats["lift"] = stats["smooth_rate"] / p_base

result = (
    stats[stats["n"] >= min_count]
    .sort_values(by=["lift", "smooth_rate", "n"], ascending=False)
)

top20 = result.head(20)[::-1]

plt.figure(figsize=(6, 4))
plt.barh(top20.index, top20["lift"])
plt.xlabel("Lift")
plt.ylabel("Слово")
plt.title("Топ-20 слов по lift")
plt.tight_layout()

plt.show()