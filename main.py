from summation import summation

if __name__=="__main__":
    x = int(input("Enter an integer: "))
    y = int(input("Enter an integer: "))

    sum_res = summation(x,y)

    print(f"Summation of {x} & {y} is: {sum_res}")