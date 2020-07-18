"""
LZW compression - dictionary creation on-the-fly
"""

user_string = input("Enter a string: ") 

dictionary = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
}
dict_counter = 5

symbol_so_far = user_string[0]

output = []
p = ""

for c in user_string:
    combined_string  = p + c
    if (combined_string in dictionary):
        p = combined_string
    else:
        output.append(dictionary[p])
        dictionary[combined_string] = dict_counter
        dict_counter += 1
        p = c

print(f"Input {user_string}")
print("(1) Output sequence: ")
print(output) 
print("")

print("(2) LZW dictionary: ")
print("string\tcode")
print("_____________")
for key, value in dictionary.items():
    print(f"{key}\t{value}")


