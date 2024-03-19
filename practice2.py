t = input("Enter a string:")
count = {}

for letter in t: 
    if letter in count:
        count[letter] += 1
    else: 
        count[letter] = 1

print("Character frequency:") 
for key, value in count.items():
            print(f"{key} : {value}")