

import urllib.request
all_words = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
words = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')
for word in words:
    word = word.decode('utf-8')
    final_word = word.strip()
    all_words.append(final_word.lower())
print("Type text; enter a blank line to end.")
to_check = input()
while to_check != "":
    list_of_checks = to_check.split()
    for word in list_of_checks:
        i = 0
        while word[i] not in alphabet:
            strip = word[i]
            word = word.lstrip(strip)
        i = -1
        while word[i] not in alphabet:
            strip = word[i]
            word = word.rstrip(strip)
        check_word = word.lower()
        if check_word not in all_words:
            print("  MISSPELLED: " + word)
    to_check = input()







