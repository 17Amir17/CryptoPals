def stringToBytes(str):
    return str.encode()

def XOR_Byte(b1, b2):
    return ord(b1) ^ ord(b2)

def XOR_Bytes_Keys(b1, key):
    enc = ''
    for i in range(0, len(b1)):
        enc += chr(XOR_Byte(b1[i], key[i % len(key)]))
    return enc

def String_To_Hex(str):
    return str.encode().hex()

plain = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"
enc = XOR_Bytes_Keys(plain, key)
print(String_To_Hex(enc))
