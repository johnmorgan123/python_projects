import pandas

def p(string):
    print(string)

dataframe = pandas.DataFrame([[2, 4, 6] , [10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
p(dataframe)

dataframe2 = pandas.DataFrame([{"Name":"John" , "Surname":"Morgan"}, {"Name":"Noah" , "Surname":"Dorta"}])
p(dataframe2)

p("-"*160)

p(dataframe.mean())
p("-"*160)

p(dataframe.Price)