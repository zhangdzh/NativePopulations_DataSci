# In this program, we want to print out specific parts of a twitter JSON file.

# 1. We start by importing the JSON library to use for this project.
# Twitter data is stored in this format
import json
from pprint import pprint

# 2. Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweet_small.json", "r")

# 3. We use the JSON library to LOAD data from the file as JSON data.
tweetData = json.load(tweetFile)

# 4. We CLOSE the file now that we have locally stored the data.
tweetFile.close()

# 5. We then PPRINT the data of ONE tweet (Use pprint instead of print to help format the output):

# 6. pprint the "text" of the first tweet:
pprint(tweetData[0]["text"])
pprint(tweetData[1]["text"])

# 7. pprint the "text" of all the tweets. (Hint: There are multiple ways!)

# 7.1 First way - accessing each index
# for index in range(len(tweetData)):
#     pprint(tweetData[index]["text"])
# 7.2 Second way - accessing each tweet
for tweet in tweetData:
    # if "Trump" in tweet["text"]:
    pprint(tweet["created_at"])
