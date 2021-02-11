def maximumUnits(boxTypes, truckSize):
        boxTypes.sort(key = lambda x:-x[1])
        maxUnit = 0
        for i in range(len(boxTypes)):
            boxCount = min(truckSize,boxTypes[i][0])
            maxUnit += boxCount*boxTypes[i][1]
            truckSize-=boxCount
        return maxUnit
        
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(maximumUnits(boxTypes,truckSize))