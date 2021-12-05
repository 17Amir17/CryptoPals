encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# The encoded string has been XOR'd by a single character

#This function with XOR by a given character
def XOR(c1, key):
    return chr(ord(c1) ^ ord(key))

#I need another function to create the whole string
def decrypt(s1, key):
    # Convert hex to string
    b1 = bytes.fromhex(s1).decode()

    decrypted = ''
    for c in b1:
        decrypted += XOR(c, key)
    
    return decrypted

# I will create a scoring function
def score(s):
    # I will score the sentance by the amount of these characters
    # e, t, a, i, o, n, s, h, and r. Since they are most popular
    chars = ['e', 's', 't', 'a', 'i', 'o', 'n', 'h', 'r']
    score = 0
    for char in chars:
        score += s.count(char) + s.count(char.upper())
    return score

# Add results to object
results = {}
for i in range(ord('A'), ord('z'), 1):
    decrypted = decrypt(encoded, chr(i))
    results[chr(i)] = [score(decrypted), decrypted]

# print them out sorted
for k,v in sorted(results.items(), key=lambda res: res[1][0], reverse=True):
    print(k, v)

# Results
# Key is 'X'
# Decrypted is "Cooking MC's like a pound of bacon"

