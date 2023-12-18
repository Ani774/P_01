q=int(input("enter staring of he range ="))
a=int(input("enter ending of he range ="))
if q%2==0:
    print("Even")
    e=q
    while e<=a:
        print(e)
        e=e+2
    f=q+1
    print("Odd")
    while f<=a:
        print(f)
        f=f+2
else:
    print("Odd")
    e=q
    while e<=a:
        print(e)
        e=e+2
    f=q+1
    print("Even")
    while f<=a:
        print(f)
        f=f+2