import pandas as pd
import numpy as np

def prepare_data(df):
    data = df.copy()
    data.columns = data.columns.str.strip()

    leakage_cols = ['averageRating', 'numVotes', 'BoxOffice']
    data = data.drop(columns=[c for c in leakage_cols if c in data.columns], errors='ignore')

    if 'runtimeMinutes' in data.columns:
        data['runtimeMinutes'] = data['runtimeMinutes'].astype(str).replace(r'\N', np.nan)
        data['runtimeMinutes'] = pd.to_numeric(data['runtimeMinutes'], errors='coerce')

    if 'startYear' in data.columns:
        data['startYear'] = data['startYear'].astype(str).replace(r'\N', np.nan)
        data['startYear'] = pd.to_numeric(data['startYear'], errors='coerce')
        data.loc[data['startYear'] <= 0, 'startYear'] = np.nan

    if 'genres' in data.columns:
        data['genres'] = data['genres'].astype(str)
        data['genres'] = data['genres'].str.replace(r"\[\]'\"", '', regex=True)
        data['genres'] = data['genres'].replace(r'\N', np.nan)

    data['num_genres'] = data['genres'].apply(
        lambda x: len(str(x).split(',')) if pd.notnull(x) else 0
    )

    data['primary_genre'] = data['genres'].apply(
        lambda x: str(x).split(',')[0].strip() if pd.notnull(x) else 'Unknown'
    )

    data['is_drama'] = data['genres'].apply(
        lambda x: int('Drama' in str(x)) if pd.notnull(x) else 0
    )
    data['is_comedy'] = data['genres'].apply(
        lambda x: int('Comedy' in str(x)) if pd.notnull(x) else 0
    )
    data['is_documentary'] = data['genres'].apply(
        lambda x: int('Documentary' in str(x)) if pd.notnull(x) else 0
    )

    if 'Country' in data.columns:
        data['is_US'] = data['Country'].apply(
            lambda x: int(any(c.strip() in ['US', 'USA', 'United States']
                              for c in str(x).split(','))) if pd.notnull(x) else 0
        )
        data['num_countries'] = data['Country'].apply(
            lambda x: len(str(x).split(',')) if pd.notnull(x) and str(x) != r'\N' else 0
        )
    else:
        data['is_US'] = 0
        data['num_countries'] = 0

    data['release_decade'] = (data['startYear'] // 10) * 10

    if 'plot' in data.columns:
        data['plot_length'] = data['plot'].apply(
            lambda x: len(str(x).split()) if pd.notnull(x) and str(x) != r'\N' else 0
        )
    else:
        data['plot_length'] = 0

    data = data.replace([np.inf, -np.inf], np.nan)
    raw_cols_to_drop = ['tconst', 'primaryTitle', 'genres', 'lead_actors_ids',
                        'plot', 'Country', 'Language', 'budget']
    data = data.drop(columns=[c for c in raw_cols_to_drop if c in data.columns],
                     errors='ignore')

    return data