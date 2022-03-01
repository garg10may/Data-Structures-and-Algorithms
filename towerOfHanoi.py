
def towerOfHanoi(height, start, temp, target):
    count =0
    if height >=1:    
        count = towerOfHanoi(height-1, start, target, temp)
        print ('moving disk from ' + start + ' to ' + target)
        count +=1
        count += towerOfHanoi(height-1, temp, start, target)
    return count


print towerOfHanoi(10,"A","B","C")