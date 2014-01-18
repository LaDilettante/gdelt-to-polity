import csv

csvfile = open('./data/brazil_2012_stories.csv', 'r')
reader = csv.reader(csvfile)

text_index = reader.next().index('RawText')

words = ["cooperation", "negotiation", "peace", "war"]
count_dict = dict((word, [0, 0]) for word in words)
story_dict = dict((word, []) for word in words)

total_article = 0
for row in reader:
    for key in count_dict.keys():
        if key in row[text_index]:
            count_dict[key][0] += 1
            story_dict[key].append(row[0])
    total_article += 1

for key in count_dict.keys():
    count_dict[key][1] =  \
        "{}{}".format((count_dict[key][0] * 100 / total_article), "%") 

print count_dict

csvoutput = open('democracy_cluster_output.csv', 'wb')
writer = csv.writer(csvoutput)

for key, value in count_dict.items():
    writer.writerow([key, value[0], value[1], story_dict[key]])
    
csvfile.close()
csvoutput.close()
