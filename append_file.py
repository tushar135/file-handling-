user = input("Enter your name: ")
with open("output.txt", "w") as file1: 
    file1.write(f"User Name: {user}")

with open("output.txt", "a") as file1:  
    file1.write("\n welcome , my world.")

with open("output.txt", "r") as file1:
    readfile = file1.read()
    print("\nFinal File Content:\n")
    print(readfile)
