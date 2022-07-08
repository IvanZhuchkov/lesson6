import functions
def main():
    n=0
    n=input("Enter positive intager: ")
    while int(n)<=0:
        print("Enter is not correct")
        n=input("Enter positive intager: ")
    f=functions.fac(n)
    n=int(n)
    print("%d! =" %n, f)
    s="""           Main Menu
       Please, select file:
    1) Lesson1.py
    2) Project.cpp
    3) Ivan.mai
    4) Exit
    """
    print(s)
    
    for m in range(3):
        n=input(">")
        if n=="1":
            print("Opening \"Lesson1.py\"...")
            continue
        elif n=="2": 
            print("Opening \"Project.cpp\"...")
            continue
        elif n=="3":
            print("Opening \"Ivan.mai\"...")
            continue
        elif n=="4":
            print("Closing...")
            break
        print("Incorrect enter")
    else:
        print("Too many incorrect data!")
    for n in range (5):
        for m in range (10):
            if m == 1:
                print(end=" ")
                continue
            if ((n == 2) & (1<m<5)):
                print(end=" ")
                continue
            if m==5 :
                print(end=" ")
                continue
            if m==8:
                if n!=1:
                    print(end=" ")
                    continue
            print("*", end="")
        print()
main()
