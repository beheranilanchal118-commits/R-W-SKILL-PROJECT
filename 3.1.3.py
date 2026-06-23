name = input("ENTER YOUR NAME ").lower()
print(f"YOUR ENTERED STRING NAME {name}")

rev = "".join(reversed(name))

print(f"YOUR RESVERED STRING IS : {rev}")

if rev == name:
    print("yes")
else:
    print("No")