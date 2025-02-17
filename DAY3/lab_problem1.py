# Write a function in Python that accepts two string parameters. The ﬁrst parameter will be a string of characters,
# and the second parameter will be the same string of characters, but they’ll be in a different order and have one
# extra character. The function should return that extra character.
# ○
# For example, if the ﬁrst parameter is “eueiieo” and the second is “iieoedue,” then the function should
# return “d.”
def extra_charc(str1, str2):
    list1 = list(str2)  # conert second string to list 
    extra_chars = [] 
    for c in str1:
        if c in list1:
            list1.remove(c)  
        else:
            extra_chars.append(c)   #meaning is an  ectra char  in str1 and not str2
    return extra_chars + list1  
str1 = "nouran"
str2 = "noour"
print(extra_charc(str1, str2))  
