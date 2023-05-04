# Prompt user for input
string = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
freq = {}

# Iterate over each character in the string
for char in string:

    # Check if the character is already in the dictionary
    if char in freq:
        # If it is, increment the count
        freq[char] += 1
    else:
        # If it's not, add it to the dictionary with a count of 1
        freq[char] = 1

# Iterate over each key-value pair in the dictionary and print the result
for char, count in freq.items():
    print(f"{count} {char}'s")