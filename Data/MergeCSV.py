import pandas as pd

filenames = ["ScoreBoardFinal2013.csv","ScoreBoardFinal2014.csv","ScoreBoardFinal2015.csv"]

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )
combined_csv.to_csv("ScoreBoardFinal1.csv", index=False )