theString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# The string is in hex (base 16)
# I will convert it to a regular string using builtin python methods
decoded = bytes.fromhex(theString)
# Now I will encode it into base64 using base64 library
import base64
encodedToBase64 = base64.b64encode(decoded)
print(encodedToBase64)