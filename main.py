import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'dwarf_stars.csv'

data1 = []
data2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data1.append(row)

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data2.append(row)

headers1 = data1[0]
headers2 = data2[0]

planet_data1 = data1[1:]
planet_data2 = data2[1:]

headers = headers1 + headers2

planet_data =[]

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])


with open("final_data.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)