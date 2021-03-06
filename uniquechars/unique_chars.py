# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(string):
    dict_of_chars = {}
    for char in string:
        keys = dict_of_chars.keys()
        if char in keys:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1
    for key in list(dict_of_chars.keys()):
        if dict_of_chars[key] > 1:
            del dict_of_chars[key]
    return list(dict_of_chars.keys())

print(unique_characters('anagram'))