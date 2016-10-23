#Given two strings find the longest common subsequence between them


def LCS(s1, s2, d = {}):
    try:
        return d[(s1,s2)]
    except:
        if s2.find(s1) != -1:
            d[(s1,s2)] = s1
            return s1
        if s1 == '':
            d[(s1,s2)] = ''
            return ''
        result1 = LCS(s1[1:], s2)
        result2 = LCS(s1[:-1], s2)
        if len(result1) > len(result2):
            return result1
        else:
            return result2

print LCS('tanmayorangebananaabcdef', "elepltanmabananaakjlkjkojhanbcorangejant")


def LCS(s1, s2, d = {}):
    if s2.find(s1) != -1:
        return s1
    if s1 == '':
        return ''
    result1 = LCS(s1[1:], s2)
    result2 = LCS(s1[:-1], s2)
    if len(result1) > len(result2):
        return result1
    else:
        return result2

print LCS('tanmayorangebananaabcdef', "elepltanmabananaakjlkjkojhanbcorangejant")
