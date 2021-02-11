# Twilio customers sometimes request to purchase vanity phone numbers. These vanity numbers are designed to be unique to the customer's brand and memorable to their end user. An example of this is 1-800-FLOWERS, which translates to 1-800-3569377. Here, each letter in the vanity code (FLOWERS) corresponds to a digit on the T9 keypad map. So, F maps to 3, L to 5, O to 6 and so on, giving us 3569377. Customers typically search Twilio's phone number inventory for such vanity codes.

# Given an array of one or more vanity codes and an array of phone numbers, write a function to find all phone numbers that match one or more vanity codes. The output must be a sorted array of unique phone numbers from the input array of numbers.

# Function Description
# Complete the function vanity in the editor below.
# vanity has the following parameter(s):
# codes[codes[0]....codes[c-1]]: an array of strings (vanity codes) numbers[numbers[0],...numbers(n-1)]: an array of strings (phone numbers) vanity should return a sorted array of phone numbers that match one or more vanity codes.

# Constraints: 

# • The input numbers array may have repeat elements.
# • The output must be a sorted array of unique numbers.
# • Vanity codes will only consist of uppercase letters (A-Z).
# • All vanity codes will be of shorter length than all phone numbers.
# • The output array should be subset of the input array of phone numbers.
# • Vanity codes can appear anywhere in the number, including country or area codes.
# • Phone numbers will be in the E.164 format i.e. a plus (+) followed by up to 15 digits (0-9).

# Input: 3
# TWLO
# CODE
# HTCH
# 5
# +17474824380
# +14157088956
# +919810155555
# +15109926333
# +1415123456

# Output:
# +14157088956
# +15109926333
# +17474824380

# Explanation:
# TWLO matches +14157088956
# (+1415708-TWLO)

# CODE matches +15109926333
# (+151099CODE-3)

import math
import os
import random
import re
import sys

# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#
def vanity(codes, numbers):
    # Write your code here
    list1 = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    num1=[]

    for i in codes:
        i = i.lower()
        num = ""
        for j in i:
            if j in list1[0]:
                num = num + '2'
            elif j in list1[1]:
                num = num + '3'
            elif j in list1[2]:
                num = num + '4'
            elif j in list1[3]:
                num = num + '5'
            elif j in list1[4]:
                num = num + '6'
            elif j in list1[5]:
                num = num + '7'
            elif j in list1[6]:
                num = num + '8'
            elif j in list1[7]:
                num = num + '9'
        num1.append(num)    
    # print(num1)
    result = []
    flag=-1
    for c in num1:
        for i in numbers:
            flag = i.find(c)
            if (flag !=-1) and (i not in result):
                result.append(i)
                flag=-1
    result = sorted(result)    
    return result

x = vanity(["TWLO","CODE","HTCH"],["+17474824380", "+14157088956" , "+919810155555",  "+15109926333", "+1415123456"])
print(x)