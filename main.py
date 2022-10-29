from summation import summation
from multiplication import multiplication

if __name__=="__main__":
    x = int(input("Enter an integer: "))
    y = int(input("Enter an integer: "))

    sum_res = summation(x,y)
    mult_res = multiplication(x,y)
    print(f"Summation of {x} & {y} is: {sum_res}")
    print(f"Multiplication of {x} & {y} is: {mult_res}")