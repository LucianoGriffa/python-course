import csv;

with open('CSV_Archives/data.csv') as archive:
  reader = csv.reader(archive);
  for i in reader:
    print(i)