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
# but thought iteratively, O(n^3) time complexity
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

print(LCS("lnaab", "banannal")) 