import matplotlib.pyplot as plt
import csv
import numpy as np
import time
import pandas as pd
f = open("Dataset/us-marriages-divorces-1867-2014.csv")
df = pd.DataFrame.from_csv("Dataset/us-marriages-divorces-1867-2014.csv")
YEAR = []
class Dataset:

    def __init__(self, data):
        self.data = data
    def filter_year_mar(self,value1, value2):
        output = []
        YEAR.clear()
        for index, row in df.iterrows():

            if index.year >=value1 and index.year<=value2:
                YEAR.append(index.year)
                output.append(row["Marriages"]/row["Population"])
        return output
    def filter_year_di(self, value1,value2):
        output = []
        for index,row in df.iterrows():
            if index.year >=value1 and index.year<=value2:
                output.append(row["Divorces"]/row["Population"])
        return output
    def plot(self, column1,column2,column3,label):
        plt.plot(column1, column2)
        plt.plot(column1, column3)
        plt.xlabel("Year")
        plt.ylabel("Rate")
        plt.legend(label)
        plt.show()

d = Dataset(df)
rate_ma = d.filter_year_mar(1867,1880)
print(YEAR)
rate_di = d.filter_year_di(1867,1880)
label=["Rate of marriages between 1867 to 1880","Rate of divorces betwwen 1867 to 1880"]
d.plot(YEAR,rate_ma,rate_di,label)

d1 = Dataset(df)
rate_ma1 = d.filter_year_mar(1875,1881)
print(YEAR)
rate_di1 = d.filter_year_di(1875,1881)
label1=["Rate of marriages between 1875 to 1881","Rate of divorces betwwen 1875 to 1881"]
d1.plot(YEAR,rate_ma1,rate_di1,label1)
