# a = [5,4,6,5,2,7]
# b = [5,46335,90039,24796,87808,17739]
# truck_size = 610563
# # Method 1
# c = []
# c.extend([b[i] for i in range(len(a)) for j in range(a[i])]) 
# c.sort(reverse=True)
# print(sum(c[:truck_size]))

# %time
# Method 2
def getMaxUnits(boxes,unitsPerBox,truckSize):
    sum=0
    totBox=0
    for i in range(truckSize):
        if(unitsPerBox != [] and totBox<=truckSize):
            maxBox = max(unitsPerBox)
            pos = unitsPerBox.index(maxBox)
            if boxes[pos]!=0:
                sum = sum+maxBox
                totBox=totBox+1
                boxes[pos]=boxes[pos]-1
                if boxes[pos]==0:
                    del boxes[pos]
                    del unitsPerBox[pos]
    return sum   
boxes=[1,2,3] #boxes
unitsPerBox=[3,2,1] #unitsPerBox
truckSize = 3
# boxes=[3,1,6] #boxes
# unitsPerBox=[2,7,4] #unitsPerBox
# truckSize = 6

res = getMaxUnits(boxes,unitsPerBox,truckSize)
print(res)