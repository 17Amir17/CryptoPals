def stringToBytes(str):
    return str.encode('utf-8')

def bytesToBits(b1):
    bits = ''
    for b in b1:
        bts = bin(b)
        for bt in bts:
            bits += bt
    return bits

def getHammingDistance(s1, s2):
    if(len(s1) != len(s2)):
        return None

    s1 = stringToBytes(s1)
    s2 = stringToBytes(s2)
    
    bits1 = bytesToBits(s1)
    bits2 = bytesToBits(s2)

    bits = len(bits1)
    bits2Len = len(bits2)

    dist = 0
    if bits < bits2Len:
        dist = bits2Len - bits
    else:
        dist = bits - bits2Len
        bits = bits2Len

    for i in range(0, bits):
        dist += int(bits1[i] != bits2[i])
        
    return dist

print(getHammingDistance('this is a test', 'wokka wokka!!!'))


