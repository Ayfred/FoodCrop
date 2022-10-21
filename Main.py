import pandas

dataframe = pandas.read_csv("FeedGrains.csv")

for index, row in dataframe.iterrows():
    column_value = row['SC_GroupCommod_Desc']
    # Colonne 4, correspond a "SC_Commodity_Desc"
    #column_value_2 = row[4]
    #print(column_value_2)é
print(column_value)


