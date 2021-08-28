import csv
import os

print(os.getcwd())
data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data)
data_lines = list(csv_data)

print(len(data_lines))

#for line in data_lines[:5]:
    #print(line)

print(data_lines[10][3])

all_emails = []

for line in data_lines[1:]:
    all_emails.append(line[3])

print(all_emails)

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])

print(full_names)

file_to_output = open('to_save_file.csv', mode='w', newline='')

csv_writer = csv.writer(file_to_output, delimiter=',')

#csv_writer.writerow(['a', 'b', 'c'])
#csv_writer.writerows([['1', '2', '3'],])
#csv_writer.writerows(([['1', '2', '3'],['4', '5', '6']]))


#this puts the users input into the new file 100 times

userinput = input("enter what u want to put in the new file!")

for i in range(100):
    csv_writer.writerow([userinput])

file_to_output.close()
f = open('to_save_file.csv', mode='a', newline='')
csv_writer =csv.writer(f)
csv_writer.writerow(['Goodbye!'])
f.close()