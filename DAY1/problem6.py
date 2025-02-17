# Write a function that takes a string and prints the
# longest alphabetical ordered substring occured. For
# example, if the string is 'abdulrahman' then the
# output is: Longest substring in alphabetical order is:
# abdu
word=str(input("Enter your string :"))
def longestsubstring(word):
    answer=word[0]
    longest=answer
    for i in range(1, len(word)):
        if word[i]>=word[i-1]:
            answer += word[i]
            if len(answer) > len(longest):
                longest = answer
        elif word[i]<word[i-1]:
            answer=word[i]
    print(longest)
longestsubstring(word)
 