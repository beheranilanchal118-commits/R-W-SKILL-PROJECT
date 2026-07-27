# ---------------------------------------------------------- FUNCTIONS ----------------------------------------------------------------------

def math_oper(*n):
    """THIS FUNCTION WILL DISPLAY MATHS OPERATION"""
    print("\n========== MATHS OPERATION ==========")
    print("Length   :", len(n))
    print("Maximum  :", max(n))
    print("Minimum  :", min(n))
    print("Sum      :", sum(n))


def avg_num(*n):
    """THIS FUNCTION CALCULATE AVERAGE"""
    return sum(n) / len(n)


def dupli_values(*n):
    """THIS FUNCTION WILL DISPLAY DUPLICATE VALUES"""
    l = []
    dup = []

    for i in n:
        if i not in l:
            l.append(i)
        elif i not in dup:
            dup.append(i)

    print("Duplicate Values :", dup)


def unique_numbers(*n):
    """THIS FUNCTION WILL DISPLAY UNIQUE VALUES"""
    unique = []

    for i in n:
        if i not in unique:
            unique.append(i)

    print("Unique Values :", unique)


def display_kwargs(**nila):
    """DISPLAY KEY-VALUE PAIRS"""
    print("\n========== KWARGS ==========")
    for key, value in nila.items():
        print(f"{key} : {value}")


def display_args(*n):
    """DISPLAY *ARGS"""
    print("\n========== ARGS ==========")
    print("Data :", n)


def factorial(n):
    """FACTORIAL FUNCTION"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """FIBONACCI SERIES"""
    a = 0
    b = 1

    print("Fibonacci Series :", end=" ")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()


def statistics(data):
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)

    return minimum, maximum, average


# ------------------------------------------------------- MAIN PROGRAM ----------------------------------------------------------------------

data = []

while True:

    print("\n")
    print("=" * 50)
    print("                 DATA ANALYSIS SYSTEM")
    print("=" * 50)
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Maths Operation")
    print("4. Duplicate & Unique Values")
    print("5. Args & Kwargs")
    print("6. Factorial & Fibonacci")
    print("7. Lambda Function")
    print("8. Arrays")
    print("9. Statistics & Sorting")
    print("0. Exit")
    print("=" * 50)

    try:
        choice = int(input("Enter Choice (0-9): "))
    except ValueError:
        print("Please Enter Integer Number Only.")
        input("\nPress Enter To Continue...")
        continue

    match choice:

       

        case 1:
            try:
                data = list(map(int, input("Enter Integer Numbers (Space Separated): ").split()))
                print("\nData Stored Successfully.")
            except ValueError:
                print("Invalid Input! Please Enter Integer Numbers Only.")

            input("\nPress Enter To Continue...")

        

        case 2:

            if not data:
                print("No Data Available.")
                print("Please Select Option 1 First.")
            else:
                print("\n========== DATA SUMMARY ==========")
                print("Data     :", data)
                print("Length   :", len(data))
                print("Maximum  :", max(data))
                print("Minimum  :", min(data))
                print("Sum      :", sum(data))
                print("Average  :", avg_num(*data))

            input("\nPress Enter To Continue...")



        case 3:

            if not data:
                print("Please Select Option 1 First.")
            else:
                math_oper(*data)
                print("Average :", avg_num(*data))

            input("\nPress Enter To Continue...")

       

        case 4:

            if not data:
                print("Please Select Option 1 First.")
            else:
                print("\n========== DUPLICATE & UNIQUE ==========")
                dupli_values(*data)
                unique_numbers(*data)

            input("\nPress Enter To Continue...")



        case 5:

            values = input("Enter Any Values (Space Separated): ").split()

            display_args(*values)
            display_kwargs(Name="Nilanchal", City="Surat", Course="BCA")

            input("\nPress Enter To Continue...")



        case 6:

            try:
                n = int(input("Enter Integer Number: "))

                print("Factorial :", factorial(n))
                fibonacci(n)

            except ValueError:
                print("Please Enter Integer Number Only.")

            input("\nPress Enter To Continue...")



        case 7:

            if not data:
                print("Please Select Option 1 First.")
            else:
                try:
                    value = int(input("Enter Integer Value: "))

                    greater = list(filter(lambda x: x > value, data))
                    less = list(filter(lambda x: x < value, data))
                    square = list(map(lambda x: x * x, data))

                    print("\n========== LAMBDA OUTPUT ==========")
                    print("Greater :", greater)
                    print("Less    :", less)
                    print("Square  :", square)

                except ValueError:
                    print("Please Enter Integer Number Only.")

            input("\nPress Enter To Continue...")



        case 8:

            try:
                arr = list(map(int, input("Enter 1D Array: ").split()))

                print("\n1D Array :", arr)

                row = int(input("Enter Number of Rows: "))
                col = int(input("Enter Number of Columns: "))

                arr2 = []

                print(f"\nEnter {row} Rows ({col} Values Each)\n")

                for i in range(row):

                    while True:

                        temp = list(map(int, input(f"Row {i+1}: ").split()))

                        if len(temp) == col:
                            arr2.append(temp)
                            break
                        else:
                            print(f"Please Enter Exactly {col} Values.")

                print("\n2D Array")

                for i in arr2:
                    for j in i:
                        print(j, end=" ")
                    print()

            except ValueError:
                print("Please Enter Integer Numbers Only.")

            input("\nPress Enter To Continue...")



        case 9:

            if not data:
                print("Please Select Option 1 First.")
            else:

                mn, mx, avg = statistics(data)

                print("\n========== STATISTICS ==========")
                print("Minimum    :", mn)
                print("Maximum    :", mx)
                print("Average    :", avg)
                print("Ascending  :", sorted(data))
                print("Descending :", sorted(data, reverse=True))

            input("\nPress Enter To Continue...")



        case 0:
            print("\nProgram Closed Successfully.")
            print("Thank You For Using Data Analysis System.")
            break



        case _:
            print("Invalid Choice! Please Enter Between 0 To 9.")
            input("\nPress Enter To Continue...")