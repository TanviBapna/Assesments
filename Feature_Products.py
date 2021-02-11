def featureProduct(products):
    dict1 = {}
    for i in products:
        if i not in dict1:
            dict1[i] = products.count(i)
    x = sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
    return x[-1][0]


products = ['red','red','orange','green','black','black']
print(featureProduct(products))