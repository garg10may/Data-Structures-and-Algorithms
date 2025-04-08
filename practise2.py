# Find all permutations of a string, was able to do it in single attempt. Thoguht of how will I do it on paper, converted that to code. 

def perm(text):
  result = []
  if len(text) == 1:
    return text
  for i in text: 
    taken = i
    rest = text[:i] + text[i+1:]
    for j in perm(rest):
      result.append(taken + j)
  return result
