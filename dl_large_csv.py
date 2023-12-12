import requests
import pandas as pd
from io import BytesIO


def stream_csv(url, destination):
    response = requests.get(url, stream=True)
    dfs = []
    for chunk in response.iter_content(chunk_size=1024):
        try:
            chunk_df = pd.read_csv(
                BytesIO(chunk), 
                encoding="utf-8", 
                sep=";", 
                error_bad_lines=False
            )
            dfs.append(chunk_df)
        except pd.errors.EmptyDataError:
            pass
    df = pd.concat(dfs, ignore_index=True, sort=False)
    df.to_csv(destination, index=False)

url = "https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv"
destination = "file.csv"
stream_csv(url, destination)
