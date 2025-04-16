# Find all permutations of a string, was able to do it in single attempt. Thoguht of how will I do it on paper, converted that to code. 

def perm(text):
  result = []
  if len(text) == 1:
    return text
  for i, char in enumerate(text):
    taken = char
    rest = text[:i] + text[i+1:]
    for j in perm(rest):
      result.append(taken + j)
  return result

print(perm("abc"))


# Find all combinations, first though iteratively but was able to for only constant length 
# and too many loops, recursive is indeed easier, if you get that idea take and not take will generate all combinations

def combinations(text):
  result = set()
  if len(text) == 1:
    return {'', text}
  take = text[0]
  rest = text[1:]
  temp = combinations(rest)
  for i in temp:
    result.add(take + i)
    result.add(i)
  return result

print(combinations("abc"))


# Able to do it in single attempt. thought of how to do it on paper, converted that to code.

def partitions(nos, count):
  if len(nos) == 0: return 0
  if count ==0: return 1
  if count < 0: return 0
  taken = nos[0]
  rest = nos[1:]
  return partitions(nos, count-taken) + partitions(rest, count)

print(partitions([1,2,3,4, 5,6], 6))


# Able to do it in single attempt. thought of how to do it on paper, converted that to code.
# but thought iteratively, O(n^3) time complexity, this is still incorrect we somehow need to backtrack 
# because we might even skip a character even if it matches to look for other characters, like 
# below doesn't capture BCAB since it's ends for BCB and then goies into next loop we have to say ok
# even if B matches, let's drop it and see if without it we can find other more and better length. 
# therefore it's better to think this in recursion itself and not in iteration.  Also be default even where 
# iteration is simpler, recursion is more simpler it just that sometimes it can confuse how to write out that 
# recursive approach.
def LCS(s1, s2):
  all_result = []
  for i in range(len(s1)):
    result = ''
    counter1 = i
    counter2 = 0
    while (counter1 < len(s1)) and (counter2 < len(s2)):
        char1 = s1[counter1]
        char2 = s2[counter2]
        if char1 == char2:
          result += char1
          counter1 += 1
          counter2 += 1
        else:
          counter2 += 1
    all_result.append(result)
  return all_result


# print(LCS("ABCBDAB", "BDCAB")) 


# Finally got this working :) it's same thought on paper, morning time, convert that to code. 
def LCS2(s1, s2):
  if len(s1) == 1 and len(s2) == 1:
    return s1 if s1 == s2 else ''
  all_result = []
  for j in range(len(s1)):
    for i in range(len(s2)):
      if s1[j] == s2[i]:
        results = [ s1[j] + _ for _ in LCS2(s1[j+1:], s2[i+1:])]
        all_result.extend(results)
        break

  return all_result if all_result else ''

print(LCS2("ABCBDAB", "BDCAB"))

def LCS_recursive(s1, s2):
  if len(s1) == 0 or len(s2) == 0:
    return ''
  if s1[0] == s2[0]:
    return s1[0] + LCS_recursive(s1[1:], s2[1:])
  else:
    return max(LCS_recursive(s1[1:], s2), LCS_recursive(s1, s2[1:]), key=len)

# print(LCS_recursive("ABCBDAB", "BDCAB"))
