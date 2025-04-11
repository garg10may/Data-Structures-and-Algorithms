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

print(perm("abcd"))


# Find all combinations

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

print(combinations("abcd"))



