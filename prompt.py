list=[]
n=int(input("Enter number of elements"))
print("enter the elements")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
    print(list)
    result=[]
    for i in list:
        if i>=100:
            result.append("Over")
        else:
            result.append(i)
            print (result)