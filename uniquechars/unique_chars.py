# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# Should print out:
# ["n", "g", "r", "m"]
'''
def unique_characters(word):
    unique_character_list = []
    for char in word:
        if char not in unique_character_list:
            unique_character_list.append(char)
    return unique_character_list

print(unique_characters("anagram"))
'''

def unique_characters(string):
    dict_of_chars = {}
    for char in string:
        keys = dict_of_chars.keys()
        if char in keys:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1
    return dict_of_chars

print(unique_characters('anagram'))