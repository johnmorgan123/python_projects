import os
import pandas

def p(string):
    print(string)

dataframe1 = pandas.read_json("supermarkets.json")
p(dataframe1)

p("*" * 160)
dataframe1.set_index("ID")
p(dataframe1)

dataframe2 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
p(dataframe2)

p("*" * 160)
dataframe3 = pandas.read_json("http://pythonhow.com/supermarkets.json")
p(dataframe3)

