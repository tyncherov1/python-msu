import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'data\anime-dataset-2023.csv', na_values = ['UNKNOWN'], usecols=['Genres', 'Score']).dropna()
df['Score'] = df['Score'].astype(float)
df['Genres'] = df['Genres'].astype(str).str.split(', ')

result_tb = df.explode('Genres').groupby("Genres", as_index=False).mean().sort_values('Score', ascending=False).reset_index(drop=True)

plt.bar(result_tb['Genres'], result_tb['Score'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
