list = [1,5,8,29,42,46,67,17,94,56,90]
print("List=",list)
for x in list:
    if(x%2)==0:
        list.remove(x)

print("After removing even numbers:", list)
