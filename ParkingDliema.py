def carParkingRoof(cars,k):
    sortedlist = sorted(cars)
    minimum = float('inf')
    if len(cars)==k:
        print("Minim:",len(cars))
    else:
        for i in range(len(sortedlist)-k+1):
            minimum = min(minimum,sortedlist[i+k-1]-sortedlist[i])
    print(minimum)

cars=[2,10,8,17]
k = 3
carParkingRoof(cars,k)