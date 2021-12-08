def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    ans = 0
    for i in range(31,-1,-1):
       b1= x>>i&1
       b2 = y>>i&1
       ans += not(b1==b2)
    return ans

def hammingDiff(s1, s2):
    s1Len = len(s1)
    s2Len = len(s2)
    if(s1Len != s2Len):
        return None
    diff = 0
    for i in range(0, s1Len):
        diff += hammingDistance(ord(s1[i]), ord(s2[i]))
    return diff

print(hammingDiff('this is a test', 'wokka wokka!!!'))
