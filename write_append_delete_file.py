#Write, append and delete in a file

#write
"""
with open ("nurlesenschreiben.txt", "w") as file:
    file.write("Here you see the students of KU:\n")
    students = ["Jana", "Alan", "Ellie", "Sophie", "Rowan", "Jake", "Bill", "Ben"]
    for student in students:
        file.write(student+"\n")
"""

#"""
#show
with open ("nurlesenschreiben.txt", "r") as file:
    for line in file:
        print(line.strip())
#"""

"""
#append
with open ("nurlesenschreiben.txt", "a") as file:
    student = "Bianca"
    file.write(student+"\n")

"""
"""
#delete
with open("nurlesenschreiben.txt", "r") as file:
    lines = file.readlines()
with open("nurlesenschreiben.txt", "w") as file:
    for line in lines:
        if line.strip("\n") != "Jana":
            file.write(line)
"""
