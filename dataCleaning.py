import pandas as pd
import csv
df=pd.read_csv("final.csv")

df.drop(['Unnamed: 0','star name2','distance2','mass2','radius2','Unnamed: 5'],axis=1,inplace=True)
finalData=df.dropna()
finalData.reset_index(drop=True,inplace=True)
finalData.to_csv("CleanedData.csv")