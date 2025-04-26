import time
from Addition import addition
from Addition import addition_of
from Subtraction import subtraction
from Subtraction import subtraction_of
from Multiplication import multiplication
from Multiplication import multiplication_of
from Adjoint_matrix import adj2x2
from Adjoint_matrix import adj3x3


print("What you chose Matrix \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.Adj a in Matrix")

try:
    Chose_Arithmetic = int(input("Enter The Perform of Matrix: "))
except ValueError:
    print("Error: Your Value is wrong you re-check the value: ")
except ZeroDivisionError:
    print("Error: Your No. is (0) Re-Enter the the No. (1/2/3/4)")
else:  # Run this block only if no exception occurs



    if Chose_Arithmetic == 1:
        print("You chose a Addition of matrix!")
        print("What You choose a matrix 1.(2x2) / 2.(3x3)")

        try:
            chose_ordr = int(input("Enter The order of Matrix: "))
        except ValueError:
            print("Error: Your Value is wrong you re-check the value: ")
        except ZeroDivisionError:
            print("Error: Your No. is (0) Re-Enter the the No. (1/2)")
            if chose_ordr == 1:
                print("You chose a 2x2 order in addition of matrix")
                addition()



            elif chose_ordr == 2:
                print("You chose a 3x3 order in addition of matrix")
                addition_of()



    elif Chose_Arithmetic == 2:
        print("You chose a Subtraction of Matrix")
        print("What you chose a matrix 1.(2x2) / 2.(3x3)")

        try:
            chose_ord = int(input("Enter The order of Matrix: "))
        except ValueError:
            print("Error: Your Value is wrong you re-check the value: ")
        except ZeroDivisionError:
            print("Error: Your No. is (0) Re-Enter the the No. (1/2)")


        if chose_ord == 1:
            print("You Chose a 2x2 order for Subtraction Matrix")
            subtraction()


        elif chose_ord ==2:
            print("You can chose 3x3 order for subtraction!")
            subtraction_of()




    elif Chose_Arithmetic == 3:
        print("You chose a multiplication of matrix")
        print("What you chose a matrix 1.(2x2) / 2.(3x3)")

        try:
            Chose_orde = int(input("Enter The order of Matrix: "))
        except ValueError:
            print("Error: Your Value is wrong you re-check the value: ")
        except ZeroDivisionError:
            print("Error: Your No. is (0) Re-Enter the the No. (1/2)")


        if Chose_orde == 1:
            print("You chose  2x2 order matrix for multiplication ")
            multiplication()


        elif Chose_orde == 2:
            print("You Chose 3x3 order matrix for multiplication ")
            multiplication_of()

    elif Chose_Arithmetic == 4:
        print("You Chose a Adj A")
        print("What you chose for Adj A 1.(2x2) | 2.(3x3)")


        try:
            Chose_order = int(input("Enter The order of Matrix: "))
        except ValueError:
            print("Error: Your Value is wrong you re-check the value: ")
        except ZeroDivisionError:
            print("Error: Your No. is (0) Re-Enter the the No. (1/2)")


        if Chose_order == 1:
            print("you Chose a 2x2 matrix for adj a!")
            adj2x2()

        if Chose_order == 2:
            print("You chose a 3x3 matrix for adj a!")
            adj3x3()



