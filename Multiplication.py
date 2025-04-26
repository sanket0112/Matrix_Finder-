import time

def multiplication ():
    print("\nEnter values for the first 2x2 matrix:")
    a1 = int(input("Enter value a1: "))
    a2 = int(input("Enter value a2: "))
    a3 = int(input("Enter value a3: "))
    a4 = int(input("Enter value a4: "))

    # Second matrix input
    print("\nEnter values for the second 2x2 matrix:")
    b1 = int(input("Enter value b1: "))
    b2 = int(input("Enter value b2: "))
    b3 = int(input("Enter value b3: "))
    b4 = int(input("Enter value b4: "))

    # Result matrix
    r1 = (a1 * b1) + (a2 * b3)
    r2 = (a1 * b2) + (a2 * b4)
    r3 = (a3 * b1) + (a4 * b3)
    r4 = (a3 * b2) + (a4 * b4)

    print("\nResultant Matrix:")
    print(f"|{r1} {r2}|")
    print(f"|{r3} {r4}|\n")
    # Get current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Write to file
    with open("Multiplication_Matrices.txt", "a") as f:
        f.write("Matrix A:\n")
        f.write(f"|{a1} {a2}|\n|{a3} {a4}|\n\n")
        f.write("Matrix B:\n")
        f.write(f"|{b1} {b2}|\n|{b3} {b4}|\n\n")
        f.write("Resultant (A * B):\n")
        f.write(f"|{r1} {r2}|\n|{r3} {r4}|\n\n")
        f.write(f"Saved on: {current_time}\n")

        f.write("-" * 30 + "\n\n")



def multiplication_of():
    print("\nEnter values for the first 3x3 matrix:")
    a1 = int(input("Enter the first value: "))
    a2 = int(input("Enter the Second value: "))
    a3 = int(input("Enter the Third value: "))
    a4 = int(input("Enter the Four value: "))
    a5 = int(input("Enter the Five value: "))
    a6 = int(input("Enter the Six value: "))
    a7 = int(input("Enter the Seven value: "))
    a8 = int(input("Enter the Eight value: "))
    a9 = int(input("Enter the nine value: "))

    print("\nEnter values for the second 3x3 matrix:")
    b1 = int(input("Enter the first value: "))
    b2 = int(input("Enter the Second value: "))
    b3 = int(input("Enter the Third value: "))
    b4 = int(input("Enter the Four value: "))
    b5 = int(input("Enter the Five value: "))
    b6 = int(input("Enter the Six value: "))
    b7 = int(input("Enter the Seven value: "))
    b8 = int(input("Enter the Eight value: "))
    b9 = int(input("Enter the nine value: "))

    r1 = ((a1 * b1) + (a2 * b4) + (a3 * b7))
    r2 = ((a1 * b2) + (a2 * b5) + (a3 * b8))
    r3 = ((a1 * b3) + (a2 * b6) + (a3 * b9))  # done
    r4 = ((a4 * b1) + (a5 * b4) + (a6 * b7))
    r5 = ((a4 * b2) + (a5 * b5) + (a6 * b8))
    r6 = ((a4 * b3) + (a5 * b6) + (a6 * b9))  # done
    r7 = ((a7 * b1) + (a8 * b4) + (a9 * b7))
    r8 = ((a7 * b2) + (a8 * b5) + (a9 * b8))
    r9 = ((a7 * b3) + (a8 * b6) + (a9 * b9))
    # Display Result
    print("\nResultant Matrix (A * B):")
    print(f"|{r1} {r2} {r3}|")
    print(f"|{r3} {r5} {r6}|")
    print(f"|{r7} {r8} {r9}|\n")

    # Save to file
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("3x3_Multiplication.txt", "a") as f:
        f.write("Matrix A:\n")
        f.write(f"|{a1} {a2} {a3}|\n|{a4} {a5} {a6}|\n|{a7} {a8} {a9}|\n\n")
        f.write("Matrix B:\n")
        f.write(f"|{b1} {b2} {b3}|\n|{b4} {b5} {b6}|\n|{b7} {b8} {b9}|\n\n")
        f.write("Resultant (A * B):\n")
        f.write(f"|{r1} {r2} {r3}|\n|{r4} {r5} {r6}|\n|{r7} {r8} {r9}|\n\n")
        f.write(f"Saved on: {current_time}\n")
        f.write("-" * 40 + "\n\n")

        print(" 3x3 Addition result saved to '3x3_Multiplication.txt'")


