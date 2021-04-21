import school_scores
list_of_record = school_scores.get_all()

# print(list_of_record[0]["GPA"])


# for dictNumber in range(len(list_of_record)):
#     print(list_of_record[dictNumber]["State"]["Name"]+":",  list_of_record[dictNumber]["Year"], "\n",  list_of_record[dictNumber]["Total"]["Test-takers"], "test-takers")

# for dictNumber in range(len(list_of_record)):
#     print(list_of_record[dictNumber]["Total"]["Test-takers"])

#verbal/math scores for females
print("Female scores:")
for dictNumber in range(len(list_of_record)):
    print(list_of_record[dictNumber]["State"]["Name"]+":")
    print("Verbal:", list_of_record[dictNumber]["Gender"]["Female"]["Math"],"\nMath:", list_of_record[dictNumber]["Gender"]["Female"]["Verbal"])
