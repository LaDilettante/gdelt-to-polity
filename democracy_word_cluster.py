import csv
import re

csvfile = open('./data/brazil_2012_stories.csv', 'r')
reader = csv.reader(csvfile)

# The column containing stories is called "RawText"
text_index = reader.next().index('RawText')

# Supply the words we want to count
words = ["cooperation", "negotiation", "peace", "war"]

# Create the dictionary. count_dict stores the frequency, 
# story_dict stores the indices of stories containing wanted words
count_dict = dict((word, [0, 0]) for word in words)
story_dict = dict((word, []) for word in words)

total_article = 0
for row in reader:
    stories_words = re.findall(r"[\w]+", row[text_index])
    for key in count_dict.keys():
        if key in stories_words:
            count_dict[key][0] += 1
            story_dict[key].append(row[0])
    total_article += 1

for key in count_dict.keys():
    count_dict[key][1] =  \
        "{}{}".format((count_dict[key][0] * 100 / total_article), "%") 

print count_dict

# Write frequency and stories indices to a csv
csvoutput = open('democracy_cluster_output.csv', 'wb')
writer = csv.writer(csvoutput)
for key, value in count_dict.items():
    writer.writerow([key, value[0], value[1], story_dict[key]])

# Closing files
csvfile.close()
csvoutput.close()
