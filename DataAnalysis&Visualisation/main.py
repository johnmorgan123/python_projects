import pandas

def p(x):
    print(x)

data = pandas.read_csv("reviews.csv")

#print(data)

print(data.head())
print(data.shape)
print(data.columns)
print(data.hist('Rating'))

p(data.iloc[3])

p('*'*160)

p(data.iloc[1:3])
p('*'*160)

p(data['Course Name', 'Rating'].iloc[1:3])

p('*'*160)
p(data['Rating'].iloc[2])
p(data.at[2, 'Rating'])



#One condition
p(data[data['Rating'] > 4])

#average rating
data['Rating'].mean()

#average for a particular course
data[data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications']

#average for a particular time
data[(data['Timestamp'] >= datetime(2020, 1, 1, tzinfo=utc)) &
     (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc))]['Rating'].mean

#average rating for a particular period for a particular course
data[(data['Timestamp'] >= datetime(2020, 1, 1, tzinfo=utc)) &
     (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc)) &
     (data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications')['Rating'].mean()

#average of uncommented ratings
data[data['Comment'].isnull()]['Rating'].mean()

#average of commented ratings
data[data['Comment'].notnull()]['Rating'].mean()

#number of uncommented ratings
data[data['Comment'].isnull()]['Rating'].count()

#number of commented ratings
data[data['Comment'].notnull()]['Rating'].count()

#number of comments containing a certain word
data[data['Comment'].str.contains('accent', na=False)]['Rating'].count()

#average of commented ratings with "accent" in comment
data[data['Comment'].str.contains('accent', na=False)]['Rating'].mean
