import os

#This function with XOR by a given character
def XOR(c1, key):
    return chr(ord(c1) ^ ord(key))

#I need another function to create the whole string
def decrypt(s1, key):
    # Convert hex to string
    b1 = bytes.fromhex(s1).decode('latin-1')

    decrypted = ''
    for c in b1:
        decrypted += XOR(c, key)
    
    return decrypted

# I will create a scoring function
def score(s):
    # I will score the sentance by the amount of these characters
    # e, t, a, i, o, n, s, h, and r. Since they are most popular
    chars = ['e', 's', 't', 'a', 'i', 'o', 'n', 'h', 'r', ' ']
    score = 0
    for char in chars:
        score += s.count(char) + s.count(char.upper())
    return score

# Get data from file
f = open(os.getcwd() + '\\basics\\c4data.txt', 'r')
strings = f.read().split('\n')
f.close()

totalResults = {}
# Go over all strings and try find its key
for s in strings:
    # Get results
    results = {}
    for i in range(ord('A'), ord('z'), 1):
        decrypted = decrypt(s, chr(i))
        results[chr(i)] = [score(decrypted), decrypted]
    # Get best result

    letter, arr = max(results.items(), key=lambda res: res[1][0])
    totalResults[arr[1]] = [arr[0], letter];

# print them out sorted
for k,v in sorted(totalResults.items(), key=lambda res: res[1][0]):
    print(k, v)
