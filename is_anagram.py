def is_anagram(first_string, second_string):
    # Your code goes here
    if len(first_string) != len(second_string):
        return False
    
    letters1 = ""
    letters2 = ""
    for char in first_string.lower():
        letters1 += char if char.isalpha() else ""
    for char in second_string.lower():
        letters2 += char if char.isalpha() else ""
    
    return (sorted(letters1) == sorted(letters2))

str1 = "Eleven plus two?"
str2 = "One plus twelve!"
str3 = "A cinnamon roll?"
str4 = "No canola oil, Mr.!"
print(is_anagram(str1, str2))
print(is_anagram(str3, str4))