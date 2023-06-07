# Health Management System----------->>>

print("Welcome to Princy's Health Management System ")
client_name = ["Harry", "Rohan", "Hammad"]


def getdate():
    import datetime
    return datetime.datetime.now()


time1 = str(getdate())
i = 1
for item in client_name:
    print(f"{i}. {item}")
    i = i + 1
n = input("Enter client's name: ")
a = int(input("Enter what you want to do, 1 for log and 2 for retrieve : "))
b = input("Enter what you want to do, D for diet and E for exercise : ")

if n == "Harry" and a == 1 and b == "D":
    with open("Harry Diet.txt", "a") as f1:
        f1.write(" \n")
        f1.write(time1 + "   - ")
        c = input("\nwrite what you want to add in your diet\n")
        f1.write(f"{c}\n")

elif n == "Rohan" and a == 1 and b == "D":
    with open("Rohan Diet.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time1 + "   - ")
        c = input("\nwrite what you want to add in your diet\n")
        f2.write(f"{c}\n")

elif n == "Hammad" and a == 1 and b == "D":
    with open("Hammad Diet.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time1 + "   - ")
        c = input("\nwrite what you want to add in your diet\n")
        f3.write(f"{c}\n")

elif n == "Harry" and a == 1 and b == "E":
    with open("Harry Exercise.txt", "a") as f1:
        f1.write(" \n")
        f1.write(time1 + "   - ")
        c = input("\nwrite what you want to add in your diet\n")
        f1.write(f"{c}\n")

elif n == "Rohan" and a == 1 and b == "E":
    with open("Rohan Exercise.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time1 + "   - ")
        c = input("\nwrite what you want to add in your diet\n")
        f2.write(f"{c}\n")

elif n == "Hammad" and a == 1 and b == "E":
    with open("Hammad Exercise.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time1 + "   - ")
        c = input("\nwrite what you want to add in your diet\n")
        f3.write(f"{c}\n")

elif n == "Harry" and a == 2 and b == "D":
    with open("Harry Diet.txt", "rt") as f4:
        print(f4.read())

elif n == "Rohan" and a == 2 and b == "D":
    with open("Rohan Diet.txt", "rt") as f5:
        print(f5.read())

elif n == "Hammad" and a == 2 and b == "D":
    with open("Hammad Diet.txt", "rt") as f6:
        print(f6.read())

elif n == "Harry" and a == 2 and b == "E":
    with open("Harry Diet.txt", "rt") as f4:
        print(f4.read())

elif n == "Rohan" and a == 2 and b == "E":
    with open("Rohan Diet.txt", "rt") as f5:
        print(f5.read())

elif n == "Hammad" and a == 2 and b == "E":
    with open("Hammad Diet.txt", "rt") as f6:
        print(f6.read())
