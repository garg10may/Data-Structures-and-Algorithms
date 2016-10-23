

print '_'*120
def pascalRow(previousRow):
    row = [1]
    for i in range(len(previousRow)-1):
        row.append(previousRow[i] + previousRow[i+1])
    row.append(1)
    return row

def pascalTriange(n):
    result =[1]
    t=[]
    t.append(result)
    for i in range(n):
        result = pascalRow(result)
        t.append(result)
    return t

def format(n):
    count =0
    traingle = pascalTriange(n)
    for count, row in enumerate(traingle):
        print ' '*(n-count),
        for i in row:
            print i,
        print

print pascalRow([1,2,1])
print pascalTriange(5)
format(5)
