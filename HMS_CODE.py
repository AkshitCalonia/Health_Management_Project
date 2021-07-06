inp = int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad : "))

if inp == 1:

    while (1):
        print("Hello Harry, which thing you want to look up for you ? (Diet/Exercise/Nothing)")

        har_diet_exercise = input()

        if har_diet_exercise =="Diet":
            f = open("Harry's diet.txt", "r")
            print(f.readline())
            print(f.readline())
            print(f.readline())
            print(f.readline())
            f.close()

        if har_diet_exercise == "Exercise":
            f = open("Harry's exercise.txt", "r")
            print(f.readline())
            print(f.readline())
            print(f.readline())
            print(f.readline())
            print(f.readline())
            print(f.readline())
            f.close()
            continue
        if har_diet_exercise == "Nothing":
            print("OK ! Thank you for visiting us")

            print("Press 1 for Harry, 2 for Rohan, 3 for Hammad")
            inp = int(input())
            break


if inp == 2:

        while (1):

            if inp == 2:
                print("Hello Rohan, which thing you want to look up for you ? (Diet/Exercise/Nothing)")
                R_diet_exercise = input()
            if R_diet_exercise =="Diet":
                f = open("Rohan's diet.txt", "r")
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                f.close()

            if R_diet_exercise == "Exercise":
                f = open("Rohan's exercise.txt", "r")
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                f.close()
                continue
            if R_diet_exercise == "Nothing":
                print("OK ! Thank you for visiting us")

                print("Press 1 for Harry, 2 for Rohan, 3 for Hammad")
                inp = int(input())
                break

if inp == 3:

        while (1):
            print("Hello Hammad, which thing you want to look up for you ? (Diet/Exercise/Nothing)")
            ham_diet_exercise = input()

            if ham_diet_exercise =="Diet":
                f = open("Hammad's diet.txt", "r")
                print(f.readline())
                print(f.readline())
                print(f.readline())
                f.close()

            if ham_diet_exercise == "Exercise":
                f = open("Hammad's exercise.txt", "r")
                print(f.readline())
                print(f.readline())
                print(f.readline())
                f.close()
                continue

            if ham_diet_exercise == "Nothing":
                print("OK ! Thank you for visiting us")

                print("Press 1 for Harry, 2 for Rohan, 3 for Hammad")
                inp = int(input())
                break
else:
    print("Wrong Input !!")
