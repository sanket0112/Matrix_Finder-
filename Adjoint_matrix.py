# this code for Adjoint for matrix
import time

def adj2x2():
    print("\nEnter values for the first 2x2 matrix:")
    a1 = int(input("Enter value a1: "))
    a2 = int(input("Enter value a2: "))
    a3 = int(input("Enter value a3: "))
    a4 = int(input("Enter value a4: "))



# result of matrix
    r1 = a4
    r2 = -a2
    r3 = -a3
    r4 = a1


# print the answer
    print(f'|{r1} {r2}|')
    print(f'|{r3} {r4}|')


#current time Show
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")


    with  open("Adjoint_matrix_2x2","a") as f:
         # Your Qutions
            f.write("This is value for convert in adj a\n ")
            f.write(f'|{a1} {a2}|\n')
            f.write(f' |{a3} {a4}|\n\n ')

# answer print
            f.write("This is answer of adj a\n")
            f.write(f'|{r1} {r2}|\n')
            f.write(f'|{r3} {r4}|\n\n')
            f.write(f"Saved on: {current_time}\n")

            f.write("-" * 30 + "\n")
            print("this is save in Adj_matrix_2x2.txt")


def adj3x3():
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

# result in matrix     #first raw completed

    r1 = (a5*a9)-(a6*a8)
    r2 = (a4*a9)-(a6*a7)
    r3 = (a4*a8)-(a5*a7)

# Seconde raw Completed

    r4 = (a2*a9)-(a3*a8)
    r5 = (a1*a9)-(a3*a7)
    r6 = (a1*a8)-(a2*a7)

# third raw is completed

    r7 = (a2*a6)-(a3*a5)
    r8 = (a1*a6)-(a3*a4)
    r9 = (a1*a5)-(a2*a4)


# all the write there
    print("this is minors of matrix for 3x3 order ")
    print(f'|{r1} {r2} {r3}|')
    print(f'|{r4} {r5} {r6}|')
    print(f'|{r7} {r8} {r9}|')

# convert in co-factors
    print("this is your Co-feactors of matrix")

    x1 = +r1
    x2 = -r2
    x3 = +r3

    x4 = -r4
    x5 = +r5
    x6 = -r6

    x7 = +r7
    x8 = -r8
    x9 = +r9


    print(f'|{x1} {x2} {x3}|')
    print(f'|{x4} {x5} {x6}|')
    print(f'|{x7} {x8} {x9}|')


# after this is transpose the unit
    print("This is Your Finale Answer of adj a in 3x3 order  ")

    print(f'|{x1} {x4} {x7}|')
    print(f'|{x2} {x5} {x8}|')
    print(f'|{x3} {x6} {x9}|')

    # current time Show
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    with (open("3x3_order_in_adj_a.txt","a") as f):
        f.write("This is Your Qutions of 3x3 matrix\n")
        f.write(f'|{a1} {a2} {a3}|\n')
        f.write(f'|{a4} {a5} {a6}|\n')
        f.write(f'|{a7} {a8} {a9}|\n\n')

        f.write("This is minors of your Qutions!\n")
        f.write(f'|{r1} {r2} {r3}|\n')
        f.write(f'|{r4} {r5} {r6}|\n')
        f.write(f'|{r7} {r8} {r9}|\n\n')

        f.write("This is your co-fecators of minors\n")
        f.write(f'|{x1} {x2} {x3}|\n')
        f.write(f'|{x4} {x5} {x6}|\n')
        f.write(f'|{x7} {x8} {x9}|\n\n')


        f.write("this is Adj of a\n")
        f.write(f'|{x1} {x4} {x7}|\n')
        f.write(f'|{x2} {x5} {x8}|\n')
        f.write(f'|{x3} {x6} {x9}|\n\n')

        f.write(f"Saved on: {current_time}\n")
        f.write("-" * 40 + "\n\n")

    print("code is succefully save in 3x3_order_in_adj_a.txt")
