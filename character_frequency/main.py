String = input("Enter a string: ")
char_count = {}

for char in String:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():

    print(f"{count} {char}'s")
