import os
from dataLoadingAndCleaning import loadAndCleanData
from trendAnalysis import plotTrends
from statisticalAnalysis import performStatisticalTests

def main(filePath):
    data = loadAndCleanData(filePath)
    plotTrends(data)
    performStatisticalTests(data)

if __name__ == "__main__":
    filePath = "imdb_top_1000.csv"
    if os.path.exists(filePath):
        main(filePath)
    else:
        print("Dataset file not found. Fix file path.")
