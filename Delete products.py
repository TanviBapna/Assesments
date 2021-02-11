def deleteProducts(ids,m):
    x  = set(ids)
    dict1={}
    for i in x:
        dict1[i]=ids.count(i)

    test = dict1.copy()
    test = dict(sorted(test.items(), key = lambda kv:(kv[1],kv[0])))
    if m == 0:
            return len(test.keys())
    else:
        
        for key,values in test.items():
            # print(key,values)
            if values <=m and m > 0:
                test[key]= values - m
                # print("test:",test[key])
                m = m - values
                # print("m:",m)
        # print(test)
        for key,values in test.items():
            if values<=0:
                del dict1[key]
        print(dict1)
        return len(dict1)

# ids=[1,1,1,2,2,3]
# ids = [1,2,3,4]
ids = [1,1,1,1]
m=2
print(deleteProducts(ids,m))


# for key,values in test.items():
        #     if values >=m and m > 0:
        #         test[key]= values - m
        #         m = m - values
        #         if test[key]==0:
        #             del test[key] 
        #     elif m == 0:
        #         if 
        #         min = len(test.keys())