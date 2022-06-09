print("This code is made By Aditya_20BCS7545")
x = []
q = int(input("Enter the length of the list:: "))
for i in range(q):
    e = input("Enter the values in list:: ")
    x.append(e)
print("Now we are going to remove 0, 4 and 5 position from list")
x.pop(0)
x.pop(3)
x.pop(3)
print(x)
