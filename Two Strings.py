def commonString(a,b):
    for i in range(len(a)):
        if set(a[i]) & set(b[i]):
            print("YES")
        else:
            print("NO")


a = ["ab","be","cd"]
b = ["ab","bc","fg"]

commonString(a,b)  