''' Prepare a dictionary from file3.txt. '''

# Define the file path
file_path = "f3.txt"

# Initialize an empty dictionary
my_dict = {}

# Open the file and read its contents
with open(file_path, "r") as file:
    # Read each line in the file
    for line in file:
        # Split the line into key-value pairs
        key, value = line.strip().split(":")
        
        # Add the key-value pair to the dictionary
        my_dict[key] = value

# Print the dictionary
print(my_dict)
