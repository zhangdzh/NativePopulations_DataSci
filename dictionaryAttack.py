#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
file = open("dictionary.txt","r")
#dumberFile = file.read().strip().split()

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords


t = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:

# for line in (file.readlines():
# wordlist = [line.strip(",") for line in file.readlines()]
def variations(s):
    s = s.replace("4","a")
    s = s.replace("0", "o")
    s = s.replace("3", "e")
    s = s.replace("1", "i")
    return s.lower()


foundPassword = False
for line in file:
    if line.strip() == variations(t.strip()):
        print("Fuck off")
        foundPassword = True
        break
if foundPassword == False:
    print("You can use this")
# for word in range(len(wordlist)):# range(len(wordlist)):
#     if (wordlist[word]).strip() == test_password.strip():
#         print("fuck")
#     else:
#         print("u can use this (but still fuck)")
#         break

#     if wordlist[word].strip() == test_password.strip():
#         wordPresent = True
#         print("No, you can't use this")
# if (wordPresent == False):
#     print("Fine, go ahead")
