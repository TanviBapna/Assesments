# Happy Numbers

# Programming challenge description: A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

# Input:

# Your program should read lines of text from standard input. Each line contains a single positive integer, N.

# Output:

# If the number is a happy number, print 1 to standard output. Otherwise, print 0.

# For the curious, here's why 7 is a happy number: 7-49→97→130→10-→1. Here's why 22 is NOT a happy number: 22→8→64→52- >29-85–89—14542-20-4-16-37 >58–89 ...

# Test 1
# 	 Input: 1
# 	Output: 1

# Test 2
# 	Input: 7
# 	Output: 1 

# Test 3
# 	Input: 22
# 	Output: 0

def isHappy(num):
    if num==1 or num==7:
        return 1
    sum = num
    n = num
    while(sum >9):
        sum = 0
        while (n>0):
            rem = n%10
            sum = sum + (rem *rem)
            n = int(n/10)
        if sum==1 or sum==7:
            return 1
        elif sum <9:
            return 0
        n = sum

print(isHappy(13))