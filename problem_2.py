'''
Convert all the numbers in the file2.txt to text. 

    Ex: This file has numbers 1,2
    Convert it to : This file has numbers one,two
'''

# Define a dictionary to map numbers to text
number_mapping = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

# Read the contents of the file
with open("f2.txt", "r") as file:
    content = file.read()

# Replace numbers with their text representations
for number, text in number_mapping.items():
    content = content.replace(str(number), text)

# Write the modified content back to the file
with open("f2.txt", "w") as file:
    file.write(content)
