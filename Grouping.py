# Website : https://stackoverflow.com/questions/63513603/what-is-the-minimum-number-of-adjacent-swaps-needed-to-segregate-a-list-of-0s-an

def minMoves(arrs):
    count_of_ones = 0
    displacement = 0
    for v in arrs:
        if v == 1: 
            count_of_ones += 1 
        if v == 0:
            displacement += count_of_ones 

    count_of_zeroes = len(arrs) - count_of_ones
    reverse_displacement = count_of_ones * count_of_zeroes - displacement
    return min(displacement, reverse_displacement)


arrs=[1,1,1,1,0,1,0,1]
arrs = [1,1,1,1,0,0,0,0]
arrs = [1,0,1,0,0,0,0,1]
print(minMoves(arrs))