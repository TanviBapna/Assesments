def fun(suffix,input1):
    count = 0
    for i in range(len(s)):
        if s[i]==input1[i]:
            count = count+1
        else:
            break
    return count
    
def commonPrefix(inputs):
    # Write your code here
    list1 = []
    for s in inputs:
        length = len(s)
        x = 0
        for i in range(length):
            x = x + fun(s[i:length],s) 
        list1.append(x) 
    return list1

print(commonPrefix(["ababaa"]))
