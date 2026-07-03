students = []
subjects = set()

while True:
    
    
    print("----------WELCOME TO STUDENT DATA INFORMATION---------")
    
    
    print("\n1.Add")
    print("2.Show")
    print("3.Update Age")
    print("4.Delete")
    print("5.Subjects")
    print("6.Exit")

    choice = int(input("Enter Choice: "))

    match choice:

        case 1:
            id = input("ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("DOB: ")
            sub = input("Subjects: ").split(",")

            students.append({
                "id": id,
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": sub
            })

            subjects.update(sub)
            print("Student Added!")

        case 2:
            for s in students:
                print(f"\nID : {s['id']}")
                print("Name : {}".format(s["name"]))
                print("Age : %d" % s["age"])
                print("Grade :", s["grade"])
                print("DOB :", s["dob"])
                print("Subjects :", s["subjects"])

        case 3:
            id = input("Enter ID: ")
            for s in students:
                if s["id"] == id:
                    s["age"] = int(input("New Age: "))
                    print("Updated!")

        case 4:
            id = input("Enter ID: ")
            for i in range(len(students)):
                if students[i]["id"] == id:
                    del students[i]
                    print("Deleted!")
                    break

        case 5:
            print("Subjects :", subjects)

        case 6:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice")