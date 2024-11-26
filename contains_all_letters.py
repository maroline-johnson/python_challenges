from string import ascii_lowercase

def check_string(my_string):
    missing = ""
    for l in ascii_lowercase:
        if l not in my_string.lower():
            missing += l
    
    if len(missing) > 0:
         return f"The string is missing the following letters: {missing}"
    else:
        return f"The string contains all the letters of the alphabet."
    
str1 = "How quickly jumping zebras vex."
str2 = "Sphinx of black quartz, judge my vow."
print(check_string(str1))
print(check_string(str2))