import json
from pprint import pprint

file = open("completedresponses.json","r")
data = json.load(file)
file.close()


sum = 0
for item in range(len(data)):
    sum += int(data[item]["age"])

print(sum)

# pprint(data[0]["age"])
# pprint(data[1]["age"])
# pprint(data[2]["age"])
# pprint(data[3]["age"])
# pprint(data[4]["age"])
# pprint(data[5]["age"])
