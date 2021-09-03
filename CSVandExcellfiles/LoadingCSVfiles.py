import os
import pandas

def p(string):
    print(string)

dataframe1 = pandas.read_csv("supermarkets.csv")
p(dataframe1)

p("*"*160)

dataframe2 = pandas.read_csv("supermarkets-commas.txt")
p(dataframe2)

p("*"*160)
dataframe3 = pandas.read_csv("supermarkets-semi-colons.txt",sep=";") #separator needed here
p(dataframe3)

p("*" * 160)
#dataframe4 = pandas.read_csv("data.txt" , header=None)
data