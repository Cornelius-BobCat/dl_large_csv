# Function donwload large csv with Pandas and Requests

1. **Télécharger le fichier CSV en streaming :** La fonction commence par utiliser la bibliothèque `requests` pour télécharger le fichier CSV en streaming depuis l'URL spécifiée.

2. **Initialiser une liste pour stocker les DataFrames temporaires :** Une liste vide `dfs` est créée pour stocker les DataFrames temporaires extraits à partir des morceaux du fichier CSV.

3. **Itérer sur les morceaux (chunks) du fichier téléchargé :** La fonction utilise une boucle `for` pour itérer sur chaque morceau du fichier CSV téléchargé en streaming. La taille de chaque morceau est définie à 1024 octets (1 Ko) par défaut, mais cela peut être ajusté selon les besoins.

4. **Lire chaque morceau en tant que DataFrame :** La fonction utilise `pd.read_csv` pour lire chaque morceau du fichier CSV en tant que DataFrame. L'utilisation de `BytesIO(chunk)` permet de traiter le morceau comme un fichier en mémoire.

5. **Ajouter le DataFrame temporaire à la liste :** Chaque DataFrame temporaire est ajouté à la liste `dfs`.

6. **Concaténer tous les DataFrames en un seul DataFrame :** Une fois que tous les morceaux ont été lus, la fonction utilise `pd.concat` pour concaténer tous les DataFrames stockés dans la liste `dfs` en un seul DataFrame `df`.

7. **Écrire le DataFrame résultant dans un fichier CSV :** Enfin, le DataFrame résultant est écrit dans un fichier CSV spécifié par l'argument `destination`. L'index du DataFrame n'est pas inclus dans le fichier CSV (`index=False`).

[Cornélius Vincent](https://www.linkedin.com/in/corneliusvincent/)
