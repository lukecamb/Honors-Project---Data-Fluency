import matplotlib.pyplot as plt
import numpy as np

def plotTrends(data):
    #Adjust IMDb Rating for consistency with Meta Score (multiply by 10)
    data['imdb_rating'] *= 10 

    #Trend of IMDb Ratings vs Meta Score
    genreMetaScore = data.groupby('genre')['meta_score'].mean()
    genreIMDb = data.groupby('genre')['imdb_rating'].mean()
    
    #Create bar plot
    genres = genreMetaScore.index
    x = np.arange(len(genres)) * 12.0  
    width = 3.0  

    plt.figure(figsize=(14, 6))
    plt.bar(x - width / 2, genreMetaScore, width, label='Meta Score', color='skyblue', alpha=0.7)
    plt.bar(x + width / 2, genreIMDb, width, label='IMDb Rating (scaled x10)', color='orange', alpha=0.7)

    plt.title('Average IMDb Rating vs Meta Score by Genre')
    plt.ylabel('Rating/Score')
    plt.xlabel('Genre')
    plt.xticks(x, genres, fontsize=6, rotation=90, ha='right')  
    plt.legend()
    plt.tight_layout()
    plt.show()

    #Trend of IMDb Ratings by Release Year
    releaseYearRatings = data.groupby('released_year')['imdb_rating'].mean()
    
    plt.figure(figsize=(12, 6))
    releaseYearRatings.plot(kind='line', marker='o', color='purple')
    
    plt.title('Average IMDb Rating by Release Year')
    plt.ylabel('Average IMDb Rating (scaled x10)')
    plt.xlabel('Release Year')
    plt.grid(True)
    plt.tight_layout()
    plt.show()






