import csv

csvfile = open('./data/brazil_2012_stories.csv', 'r')
reader = csv.reader(csvfile)

text_index = reader.next().index('RawText')

word = "cooperation"

count = 0
for row in reader:
	if word in row[text_index]:
		count += 1
print count
