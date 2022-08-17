lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
for n in range(lower,upper+1):
    s=0
    temp=n
    while temp > 0:
        digit=temp%10
        s=digit**3
        temp//=10
        if n==s:
            print(n)