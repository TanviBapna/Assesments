
# Given a string that might have multiple occurrences of the same character, return the closest same character of any indicated character in the string. You are given the string s and n number of queries. In each query, you are given an index a (where 0< a <Isl) of a character, and you need to print the index of the closest same character. If there are multiple answers, print the smallest one, or if there is no such index print -1 instead.
# For example, for the string s= babab, with a given query 2 there are two matching characters at indices O and 4, each 2 away, so we choose the lower of the two: 0.
# Function Description:
# Complete the function closest in the editor below. The function must return an integer vector of size n that denotes the answer of each query.
# closest has the following parameters:
# s: the original string
# queries: an array of n integers, where the value of each element queries is an index of a character whose closest same character's index needs to be found.

# Constraints
# • Is| , lqueries|<= 10^5
# • 1<=n<= 10^5
# • s will contain only lowercase letters from the English alphabet, ascii[a-z]

# Sample Case 0
    # Sample Input 0
    # hackerrank
    # 4 
    # 1
    # 6
    # 8
    # Sample Output 0
    # -1
    # 7 
    # 5
    # -1
    # Explanation 0
    # Query #0: Character at index-4 is 'e. In this case, there is no other e present in s, we print -1. Query #1: Character at index-1 is 'a'. In this case, there is only one closest index (index-7) that contains 'a'. 
    # Query #2: Character at index-6 is 'r. In this case, there is only one closest index (index-5) that contains 'r.
    # Query #3: Character at index-8 is 'n'. In this case, there is no other 'n present in s, so we print -1.

# Sample Case 1
    # Sample Input 1
    # 1
    # 2.
    # 3
    # Sample Output 1
    # 1
    # 2
    # Explanation 1
    # Query #0: Character at index-0 is 'a' In this case, there is only one closest index (index-1) that contains a'. Query #1: Character at index:1 is 'a In this case, there are two closest indexes (index-0 and index-2) that also contain 'a.Since O is smaller than 2 we print 0. 
    # Query #2: Character at index-2 is 'a'. In this case, there are two closest indexes (index-1 and index-3) that also contain 'a Since 1 is smaller than 3 we print 1.
    # Query #3: Character at index-3 is 'a'. In this case, there is only one closest index (index-2) that contains a

# Sample Case 2
    # Sample Input 2
    # sam
    # 1
    # 1
    # Sample Output 2
    # -1
    # Explanation 2
    # Query #0: Character at index-1 is 'a'. In this case, there is no other a present in s so we print -1.


def string(s,queries):
    list1 = list(s)
    for Query in queries:
        element = list1[Query]
        # print("Element:",element)
        min1 = len(list1)
        if element in list1[Query-1::-1]:
            # print("Left:",list1[Query-1::-1].index(element))
            x = Query - list1[Query-1::-1].index(element)-1
            min1 = min(min1,x)
        if element in list1[Query+1::]:
            # print("Right:",list1.index(element,Query+1))
            min1 = min(min1,list1.index(element,Query+1))
        if min1 == len(list1):
            print("-1")
        else:
            print(min1)


# list1 = [1, 2, 3, 4, 4, 1, 1, 1, 4, 5]
s = "hackerrank"
queries = [4,1,6,8]
string(s,queries)