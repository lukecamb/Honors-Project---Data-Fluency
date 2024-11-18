import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

def performStatisticalTests(data):
    #Handle missing values
    cleanedData = data.dropna(subset=['imdb_rating', 'no_of_votes', 'meta_score'])

    #Adjust IMDb Rating for consistency with Meta Score (multiply by 10)
    cleanedData['imdb_rating'] *= 10  # Scaling IMDb rating to match Meta Score (0-100 scale)

    #Correlation of IMDb Rating vs Number of Votes
    correlationVotesRating, pValueVotesRating = stats.pearsonr(cleanedData['imdb_rating'], cleanedData['no_of_votes'])
    print("Correlation between IMDb Rating and Number of Votes: " + str(correlationVotesRating) + ", p-value: " + str(pValueVotesRating))

    #Plot of IMDb Rating vs Number of Votes
    plt.figure(figsize=(10, 6))
    plt.scatter(cleanedData['no_of_votes'], cleanedData['imdb_rating'], alpha=0.6)
    plt.title('Scatter Plot: IMDb Rating vs Number of Votes', fontsize=14)
    plt.xlabel('Number of Votes', fontsize=12)
    plt.ylabel('IMDb Rating (scaled x10)', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid()
    plt.tight_layout()
    plt.show()

    #Correlation of IMDb Rating vs Meta Score
    correlationMetaRating, pValueMetaRating = stats.pearsonr(cleanedData['imdb_rating'], cleanedData['meta_score'])
    print("Correlation between IMDb Rating and Meta Score: " + str(correlationMetaRating) + ", p-value: " + str(pValueMetaRating))

    #Plot of IMDb Rating vs Meta Score
    plt.figure(figsize=(8, 6))
    plt.scatter(cleanedData['meta_score'], cleanedData['imdb_rating'], alpha=0.6, color='green')
    plt.title('Scatter Plot: IMDb Rating vs Meta Score', fontsize=14)
    plt.xlabel('Meta Score', fontsize=12)
    plt.ylabel('IMDb Rating (scaled x10)', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid()
    plt.tight_layout()
    plt.show()

    #T-test of IMDb Ratings for Action vs Drama
    actionRatings = data[data['genre'].str.contains('Action', na=False)]['imdb_rating']
    dramaRatings = data[data['genre'].str.contains('Drama', na=False)]['imdb_rating']
    tStat, pValue = stats.ttest_ind(actionRatings, dramaRatings, nan_policy='omit')
    print("T-test for IMDb Ratings (Action vs Drama): t-statistic = " + str(tStat) + ", p-value = " + str(pValue))

    #Plot of Box Plot for IMDb Ratings (Action vs Drama)
    plt.figure(figsize=(8, 6))
    plt.boxplot([actionRatings.dropna(), dramaRatings.dropna()], labels=['Action', 'Drama'])
    plt.title('Box Plot: IMDb Ratings (Action vs Drama)', fontsize=14)
    plt.ylabel('IMDb Rating (scaled x10)', fontsize=12)
    plt.grid()
    plt.tight_layout()
    plt.show()

    #Chi-Square Test of Genre vs Meta Score
    if data['meta_score'].isnull().all() or data['meta_score'].nunique() <= 1:
        print("Meta scores are not suitable for binning.")
    else:
        genreMetaScore = pd.cut(data['meta_score'], bins=5, labels=False)
        chi2, p, _, _ = stats.chi2_contingency(pd.crosstab(data['genre'], genreMetaScore))
        print("Chi-Square Test (Genre vs Meta Score): chi2 = " + str(chi2) + ", p-value = " + str(p))





