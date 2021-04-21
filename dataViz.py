'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweet_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

polarityList = []
subjList = []
# Textblob sample:
for index in range(len(tweetData)):
    tb = TextBlob(tweetData[index]["text"])
    indPolarity = tb.polarity
    indSub = tb.subjectivity
    polarityList.append(indPolarity)
    subjList.append(indSub)

sum = 0
for pol in polarityList:
    sum += pol
avgPolarity = sum/len(polarityList)
print("The average polarity is",avgPolarity)

subsum = 0
for sub in subjList:
    subsum += sub
avgSub = subsum/len(subjList)
print("The average subjectivity is", avgSub)

# print(sum)
# print(polarityList)


#histogram
plt.subplot(1,2,1)
plt.hist(polarityList, bins=[-1.1, -.75, -.5, -.25, 0, .25, .5, .75, 1.1])
plt.title("Polarity")
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)

plt.subplot(1,2,2)
plt.hist(subjList, bins=[0, .25, .5, .75, 1.1])
plt.title("Subjectivity")
plt.axis([0, 1.1, 0, 100])
plt.show()

#worldcloud
fulltweets= ""
for item in range(len(tweetData)):
    fulltweets = fulltweets + (tweetData[item]["text"])

print(fulltweets)
