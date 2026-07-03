
-----------------------------------------------------------------PROJECT - 1-------------------------------------------------------------------------

# User Information Collector - Python Project

## 📌 Project Description

This is a beginner-friendly Python program that collects basic information from the user and displays it in a structured format.

The program takes the following inputs from the user:

- Name
- Age
- Height
- Favorite Number

It then displays:

- Entered values
- Data type of each value
- Memory address of each variable using `id()`
- Approximate birth year based on the user's age

This project helps beginners understand Python fundamentals such as variables, input/output operations, data types, type casting, string formatting, and memory management.

---

## 🎯 Learning Objectives

By completing this project, you will learn:

- How to take input from users
- How to store data in variables
- How to convert data types using type casting
- How to use `type()` function
- How to use `id()` function
- How to perform basic calculations
- How to display output using f-strings

---

## 💻 Source Code

```python
name = input("ENTER YOUR NAME : ")
age = int(input("ENTER YOUR AGE : "))
height = float(input("ENTER YOUR HEIGHT : "))
number = int(input("ENTER YOUR FAVOURITE NUMBER : "))

year = 2026 - age

print("----------------------------------------------------------")

print("NAME IS", name, "TYPE IS :", type(name), "& MEMORY ADDRESS :", id(name))
print("AGE IS", age, "TYPE IS :", type(age), "& MEMORY ADDRESS :", id(age))
print("HEIGHT IS", height, "TYPE IS :", type(height), "& MEMORY ADDRESS :", id(height))
print("NUMBER IS", number, "TYPE IS :", type(number), "& MEMORY ADDRESS :", id(number))

print("----------------------------------------------------------")

print(f"YOUR BIRTH YEAR IS APPROXIMATELY : {year} (BASED ON YOUR AGE OF {age})")

print("----------------------------------------------------------")

print("__________THANK YOU FOR PROVIDING US YOUR DATA____________")
```

---

## 🔍 Explanation of the Code

### 1. Taking User Input

```python
name = input("ENTER YOUR NAME : ")
```

The `input()` function accepts data from the user and stores it as a string.

---

### 2. Converting Age into Integer

```python
age = int(input("ENTER YOUR AGE : "))
```

The entered age is converted from string to integer using `int()`.

---

### 3. Converting Height into Float

```python
height = float(input("ENTER YOUR HEIGHT : "))
```

The entered height is converted into a floating-point number.

---

### 4. Favorite Number

```python
number = int(input("ENTER YOUR FAVOURITE NUMBER : "))
```

The favorite number is stored as an integer.

---

### 5. Birth Year Calculation

```python
year = 2026 - age
```

The program estimates the birth year based on the age entered by the user.

---

### 6. Displaying Data Types

```python
type(name)
```

Returns the data type of the variable.

Example:

```python
<class 'str'>
```

---

### 7. Displaying Memory Address

```python
id(name)
```

Returns the memory location where the variable is stored.

---

### 8. Using f-Strings

```python
print(f"YOUR BIRTH YEAR IS APPROXIMATELY : {year}")
```

f-Strings allow variables to be inserted directly into text.

---

## 📋 Sample Output

```text
ENTER YOUR NAME : Shivaji
ENTER YOUR AGE : 20
ENTER YOUR HEIGHT : 5.8
ENTER YOUR FAVOURITE NUMBER : 7

----------------------------------------------------------

NAME IS Shivaji TYPE IS : <class 'str'> & MEMORY ADDRESS : 140123456789

AGE IS 20 TYPE IS : <class 'int'> & MEMORY ADDRESS : 140123456700

HEIGHT IS 5.8 TYPE IS : <class 'float'> & MEMORY ADDRESS : 140123456600

NUMBER IS 7 TYPE IS : <class 'int'> & MEMORY ADDRESS : 140123456500

----------------------------------------------------------

YOUR BIRTH YEAR IS APPROXIMATELY : 2006 (BASED ON YOUR AGE OF 20)

----------------------------------------------------------

__________THANK YOU FOR PROVIDING US YOUR DATA____________
```

---

## 🛠 Requirements

- Python 3.x

Check installed version:

```bash
python --version
```

---

## ▶️ How to Run

### Step 1: Save the File

Save the code as:

```text
user_information.py
```

### Step 2: Open Terminal

Navigate to the project folder.

### Step 3: Run the Program

```bash
python user_information.py
```

---

## 🚀 Future Enhancements

- Add exception handling for invalid inputs
- Automatically detect the current year
- Store user data in a text file
- Create a graphical user interface (GUI)
- Generate a user report

---

## 👨‍💻 Author

**  NILANCHAL BEHERA**

Python Beginner Project  
Created for learning Python fundamentals including input handling, data types, memory addresses, and calculations.

---

⭐ If you found this project useful, consider giving it a star on GitHub!






-----------------------------------------------------------------PROJECT - 2-------------------------------------------------------------------------



# 🎓 Student Data Organizer

## 📌 Project Description
Student Data Organizer is a simple Python project that helps manage student records. Users can add, view, update, and delete student information using a menu-driven program.

This project is created using basic Python concepts and is suitable for beginners.

---

## ✨ Features
- Add Student
- Display Student Details
- Update Student Age
- Delete Student
- Display Unique Subjects
- Menu-Driven Program

---

## 🛠️ Technologies Used
- Python 3
- Match Case
- List
- Dictionary
- Set
- Tuple
- Type Casting

---

## 📚 Python Concepts Used
- Variables
- Input and Output
- List
- Tuple
- Dictionary
- Set
- String Formatting
- Match Case
- Loops
- Conditional Statements
- Type Casting
- `del` Keyword

---

## ▶️ How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder.
4. Run the program using:

```bash
python student_data_organizer.py
```

---

## 📂 Project Structure

```
Student-Data-Organizer/
│── student_data_organizer.py
│── README.md
```

---

## 👨‍💻 Author

**NILANCHAL BEHERA**

---

## 📄 License

This project is created for learning and educational purposes.
