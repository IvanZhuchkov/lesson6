def pr(i, n="X"):
    print("Number {} = {}".format(n,i))
def de(n):
    if "." in n:
        n=float(n)
        return n
    else:
        n=int(n)
        return n
def arif (a,c,b):
    try:
        a = de(a)
        b = de(b)
        r=None
        if c=="+":
         r=a+b
        elif c=="-":
            r=a-b
        elif c=="*":
            r= a*b
        elif c=="/":
            r=a/b
        elif c=="**":
            r=a**b
        elif c=="%":
         r  =a%b
        elif c=="//":
            r=a//b
        else :
            print("Incorect enter")
        if r is not None:
            return r
    except:    
        print ("Enter is not correct")

def fac (n):
    n = de(n)
    m=[1]
    if n > 0:
        for i in range(n):
            m.append(m[i]*(i+1)) 
        del m[0]
        return m[n-1]
    elif n==0:
        return 1
    else:
        print("Incorrect enter!")
    return 0


def dis(st):
    """
    This function take a string and convert it in some arifmetic expression.

For correct work you have to use space and don't enter more than one opperation.
    """
    o=0
    j=0
    for i in range(len(st)):
        if st[i]==" ":
            if o==0:
                a=st[j:i]
                j=i+1
                o=1
            elif o==1:
                op=st[j:i]
                j=i+1
                o=2
            else:
                b=st[j:i]
                j=i+1
                o=3
        
        if (i+1) == len(st):
                b=st[j:i+1]
                o=3
        if st[i]=="!":
                a=st[j:i]
                o=4
        if o==3:
                r=arif(a,op,b)
                return r
        if o==4:
               r=fac(a)
               return r
        
def main():
    x=pr(n = "N",i = 15)
    if x==None :
        print("Success")
    help(dis)
    st=input("Your expression: ")
    r=dis(st)
    print("Result: ",r)
if __name__=="__main__":
    main()