
        print("WELCOME..")
while True:

        print("1. pattern")
        print("2. analyz number")
        print("3. exit")

        choice=int(input("enter your choice: "))

        if choice == 1:
            number = int(input("Enter the number of rows: "))
            for i in range(1,number+1):
                for x in range(1,i+1):
                    print("*",end="")
                print()
                     
        elif choice == 2:
            sum=0
            start=int(input("Start number:"))
            end=int(input("End number:"))
            
            for i in range(start,end+1):
                    if i %2 == 0 :
                        print(f"number {i} is even.")
                    else:
                        print(f"number {i} is odd.")
                    sum=sum+i
            print(f"sum of {start} to {end} is= {sum}")

        elif choice == 3:
            print("thank you")
            break

        else:
            print("enter valid choice.")