# Write a Python function that checks whether a
# passed string is palindrome or not.Note: A
# palindrome is a word, phrase, or sequence that
# reads the same backward as forward, e.g., madam
# or nurses run {ignoring the spaces }.
word = str(input("Enter Your String :"))
def is_palindrome (word):
    nospace=word.replace(" ","").lower()
    return nospace==nospace[::-1]
print(is_palindrome(word))
    