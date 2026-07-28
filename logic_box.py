while True:

    print("\n=====================================================")
    print("\n ***Welcome to Pattern Generate and Number Analyze***")
    print("\n=====================================================")
    
    
    print("""
        Select An Option
        1. Generate A Pattern
        2. Analyze A Range of Numbers
        3. Exit
        -->  Write pass for skip The Choice.... 
        -->  Write continue to Skip The Condition...
    """)
    print("\n=====================================================")
    
    
    user = (input("Enter Your Choice : "))

    if user == "1":

        rows = int(input("Enter number of rows: "))
        if rows > 5:
            print("Rows limit Exceeded! Program Will be Stop ")
            break
        else:
            

            for i in range(1, rows + 1):
                print("* " *i)
        
    elif user == "2":
        print("\n=====================================================")
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        if end > start:    
            
                    total = 0

                    for i in range(start, end + 1):
                        if i % 2 == 0:
                            print(f"->Number {i} is Even")
                        else:
                            print(f"->Number {i} is Odd")

                        total += i
                    print("\n================================")
                    print(f"\n ->Sum of all numbers from {start} to {end} is: {total}")
                    print("\n================================")
        else:
                print("Starting range should be small and end range should be big")
                print("start:small  end:big")
                print("\n================================")
                break 
        
    elif user == "3":
        print("\n================================")
        print("\n Exiting The Program. Goodbye! ")
        print("\n================================")
        break
    
    elif user == "pass":
        pass
    elif user == "continue":
        print("==================================")
        print("You Press The continue so Program Will End.... Forward To the Next Condition... ")
        print("==================================")
        input("PRESS ENTER 2 TO RE- ENTER THE PROGRAM ")

    else:
        print("Invalid Choice! Please Try Again.")
    input("Press Enter To See Main Menu....") 
    
    
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        