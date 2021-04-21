names_ages = {
"Emily" : 16,
"Mom" : 43,
"Dad" : 47,
"Amy" : 15,
"Alena" : 6,
"Baylee" : 4,
"Katherine" : 15,
"Annesha" : 15,
"Chris" : 16,
"Erica" : 16,
"Monica" : 16,
}

# names_ages["Amy"] += 1
# print("Amy is", names_ages["Amy"])

#print all names_ages
# for person in names_ages:
#     print(person, names_ages[person])

sum = 0
for person in names_ages:
    sum += names_ages[person]

print("The sum of the ages is", sum)

print("The average age is", sum/len(names_ages))
