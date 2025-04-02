def palindrom(s):
    return s == s[::-1]

word = input("Enter a word: ").lower()
if palindrom(word):
    print(word, "is a palindrom.")
else:
    print(word, "is not a palindrom")