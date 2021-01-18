
# Pattern Recognition

# Programming challenge description:
# Given a pattern as the first argument and a string of blobs split by show the number of times the pattern is present in each blob and the total number of matches.

# Input:
# The input consists of the pattern ("bc" in the example) which is separated by a semicolon followed by a list of blobs ("bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32" in the example). Example input: bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32

# Output:
# The output should consist of the number of occurrences of the pattern per blob (separated by |). Additionally, the final entry should be the summation of all the occurrences (also separated by |).

# Example output: 3|2|1|2|8 where 'bc' was repeated 3 times, 2 times, 1 time, 2 times in the 4 blobs passed in. And 8 is the summation of all the occurrences (3+2+1+2 = 8)

# Test 1
# Test Input : ;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
# Expected Output:  0|0|0|0|0

# Test 2
# Test Input: b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|lbcdef23423bc32
# Expected Output : 4|2|3|2|11

# Test 3
# Test Input: aa; aaaakjlhaa| aaadsaaa |easaaad|sa
# Expected Output: 4|4|2|0|10

import sys

def doSomething(blob, pattern):
    #Write your code here
    #print(blob)
    #print(pattern)
    s=""
    sum1 =0
    if pattern =="":
        len1 = len(blob)
        for i in range(len1):
            s = s+"0|"
        s = s+"0"
    else:
        for i in blob:
            start = 0
            count = 0
            while start < len(i): 
                pos = i.find(pattern, start) 
                if pos != -1: 
                    start = pos +1
                    count += 1
                else: 
                    break 
            #print(count) 
            s = s + str(count)+"|"
            sum1 = sum1 + count
        s = s + str(sum1)
    return s

        
for line in sys.stdin:
    splitted_input = line.split(';')
    print(splitted_input)
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')
 
    result = doSomething(blobs, pattern)
    print(result)