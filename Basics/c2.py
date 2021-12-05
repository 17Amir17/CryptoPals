def XORCombine(s1, s2):
    # Unhexify
    h1 = bytes.fromhex(s1).decode('utf-8')
    h2 = bytes.fromhex(s2).decode('utf-8')
    combination = ''
    for i in range(0, len(h1)):
        combination += chr(ord(h1[i]) ^ ord(h2[i]))
    return combination.encode().hex()

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
a = '746865206b696420646f6e277420706c6179'

if(XORCombine(s1, s2) == a):
    print('Success')
else:
    print('Failed')