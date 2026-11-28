import pandas as pd

df = pd.read_csv(r'data\anime-dataset-2023.csv')
genres = {genre.strip():[] for row in df['Genres'] for genre in str(row).split(',')}

for i, n in zip(df["Genres"], df['Score']):
    try:
        n = float(n)
    except ValueError:
        continue

    for gen in {gs.strip() for gs in i.split(',')}:
        genres[gen].append(n)

for i, j in genres.items():
    genres[i] = sum(j) / len(j)

result_tb = pd.DataFrame(
    {
    'Genres' : genres.keys(),
    'Score' : genres.values()
})
result_tb = result_tb.sort_values("Score", ascending=False).reset_index(drop=True)

print(result_tb)
