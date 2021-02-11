
# def findMaxMatrixSize(arr, K):
#     # N size of rows and M size of cols
#     n = len(arr)
#     m = len(arr)
 
#     # To store the prefix sum of matrix
#     sum = [[0 for i in range(m + 1)] for j in range(n + 1)]
 
#     # Create Prefix Sum
#     for i in range(n + 1):
 
#         # Traverse each rows
#         for j in range(m+1):
#             if (i == 0 or j == 0):
#                 sum[i][j] = 0
#                 continue
 
#             # Update the prefix sum
#             # till index i x j
#             sum[i][j] = arr[i - 1][j - 1] + sum[i - 1][j] + \
#                 sum[i][j - 1]-sum[i - 1][j - 1]
 
#     # To store the maximum size of
#     # matrix with sum <= K
#     ans = 0
 
#     # Traverse the sum matrix
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
 
#             # Index out of bound
#             if (i + ans - 1 > n or j + ans - 1 > m):
#                 break
 
#             mid = ans
#             lo = ans
 
#             # Maximum possible size
#             # of matrix
#             hi = min(n - i + 1, m - j + 1)
 
#             # Binary Search
#             while (lo < hi):
 
#                 # Find middle index
#                 mid = (hi + lo + 1) // 2
 
#                 # Check whether sum <= K
#                 # or not
#                 # If Yes check for other
#                 # half of the search
#                 if (sum[i + mid - 1][j + mid - 1] +
#                     sum[i - 1][j - 1] -
#                     sum[i + mid - 1][j - 1] -
#                         sum[i - 1][j + mid - 1] <= K):
#                     lo = mid
 
#                 # Else check it in first
#                 # half
#                 else:
#                     hi = mid - 1
 
#             # Update the maximum size matrix
#             ans = max(ans, lo)
#             # print(ans)
 
#     # Print the final answer
#     return(ans )


def maxSumSubmatrix(grid, maxSum):
    if not grid or not grid[0]: return 0
        # create culmulative sum 2D array. O(n^2) pre computation
    n = len(grid)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = grid[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    #O(n^2) - worst case when k = 1, there will be n^2 operations
    def maxsum_region(k):
        total = 0
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                gross_sum = dp[i + k][j + k] #sum_od
                sum_ob = dp[i][j + k]
                sum_oc = dp[i + k][j]
                sum_oa = dp[i][j]
                net_sum = gross_sum - sum_ob - sum_oc + sum_oa
                total = max(total, net_sum)
        return total
        
    # binary search. O(log n) where n is grid size
    left, right = 0, n
    while left <= right:
        mid = left + (right - left)//2
        cur_maxsum = maxsum_region(mid)
        if mid == 0 or mid == n or cur_maxsum <= maxSum < maxsum_region(mid + 1):
            return mid 
        elif maxSum > cur_maxsum:
            left = mid + 1
        else:
            right = mid - 1

x = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
# x = [[1,1,1],[1,1,1],[1,1,1]]
# x = [[4,5],[6,7]]
print(maxSumSubmatrix(x,39))

# import bisect
# def maxSumSubmatrix(grid, maxSum):
#     row = len(grid)
#     col = len(grid[0])  
#     res = -2**31

#     for i in range(col):
#         col_sum = [0 for k in range(row)]
#         for j in range(i, col):
#             for k in range(row):
#                 col_sum[k] += grid[k][j]

#             temp = [0]
#             cur_sum = 0

#             for k in range(row):
#                 cur_sum += col_sum[k]
#                 temp_target = cur_sum - maxSum
#                 idx = bisect.bisect_left(temp, temp_target)
#                 if idx != len(temp):
#                     res = max(res, cur_sum-temp[idx])
#                 bisect.insort_left(temp, cur_sum)
        
#     return res

