import pandas as pd

def loadAndCleanData(filePath):
    #Load the dataset
    data = pd.read_csv(filePath)

    #Standardize column names
    data.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)

    #Drop rows with missing values
    data.dropna(subset=['imdb_rating', 'no_of_votes'], inplace=True)

    #Convert columns to appropriate data types
    data['released_year'] = pd.to_numeric(data['released_year'], errors='coerce')
    data['no_of_votes'] = pd.to_numeric(data['no_of_votes'], errors='coerce')

    #Fill missing metascores with mean
    data['meta_score'] = data['meta_score'].fillna(data['meta_score'].mean())

    return data

