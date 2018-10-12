def polindrom(word):
    x = word.split(" ")
    word = ''.join(x).lower()
    #print(word)
    string = word[::-1]
    #print(string)
    if word == string:
        return True
    else:
        return False

print(polindrom(input("input! ")))




