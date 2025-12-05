n1=float(input())
n2=float(input())
print("1:+  2:-  3:*  4:/")
ch=int(input("choose operation"))
if ch==1:
    print("Result:",n1+n2)
elif ch==2:
    print("Result:",n1-n2)
elif ch==3:
    print("Result:",n1*n2)
elif ch==4:
    print("Result:",n1/n2)
else:
    print("Invalid Choice")