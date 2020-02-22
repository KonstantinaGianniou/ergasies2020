number=int(input('Give a number!'))
number=number*3+1
l=len(str(number))
sum=0
if number<=9:
    sum=number
    s=number
while number>9:
    x=10**(l-1)
    if x==10:
        div=number//x
        mod=number%x
        sum=sum+div+mod
        number=mod
    elif x>10:
        div=number//x
        mod=number%x
        sum=sum+div
        number=mod
        if len(str(number))==1:
            sum=sum+mod
    l=len(str(number))
s=sum
l=len(str(s))
k=s
while s>9:
    sum=0
    s=s*3+1
    k=s
    l=len(str(k))
    while k>9:
        x=10**(l-1)
        if x==10:
            div=k//x
            mod=k%x
            sum=sum+div+mod
            k=mod
        elif x>10:
            div=k//x
            mod=k%x
            sum=sum+div
            k=mod
            if len(str(k))==1:
                sum=sum+mod
        l=len(str(k))
    s=sum       
print('The final number is:',sum) 
