text = "Swedish pop group ABBA, single SOS unique occo both palindromes."

palindromes = 0
a = text.rstrip(',.:;!?')
for word in a.split():
        a = word.rstrip(',.:;!?')
        if a.lower() == a.lower()[::-1]:
            palindromes += 1

print(palindromes)
