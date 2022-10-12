import pandas

dataframe = pandas.read_csv("D:\maxim\Documents\Python\FeedGrains.csv")


for index, row in dataframe.iterrows():
    print(index, row)
