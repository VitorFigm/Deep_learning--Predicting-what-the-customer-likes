import pandas as pd
import numpy as np
    #####pre-processing
data = pd.read_csv('Reviews.csv')
reviews = data[['ProductId','Score','UserId']]



#for simplifing, the neural network will only predict if the score is 5 or not, so 5 stars will be 1 and the other scores and unseeing items will be 0
reviews['Score'][reviews['Score']!=5]=0  
reviews['Score'][reviews['Score']==5]=1


##Limiting the DataFrame for pivoting better(it's almost impossible without it)
indexes = reviews['ProductId'].value_counts().iloc[0:2000].index
reviews.index = reviews['ProductId']
reviews = reviews.loc[indexes]

del indexes

indexes = reviews['UserId'].value_counts().iloc[0:10000].index
reviews.index = reviews['UserId']
reviews = reviews.loc[indexes]

del indexes

reviews.index = range(0,reviews.shape[0])

#pivoting

pivot = reviews.pivot_table(index='UserId',columns='ProductId',dropna=False,aggfunc=np.amax).fillna(0)


#deleting User with fell buyings
arr=pivot.mean(axis=1)*pivot.shape[1]
arr = arr[arr>=8].index
pivot = pivot.loc[arr]
del arr
#renaming cols for csv
cols = []
for i in pivot.columns:
    cols.append(i[1])

pivot.columns = cols


#generate csv
pivot.to_csv('pivot.csv')