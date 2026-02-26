target = 300
def find_closest_number ():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    num3 = int(input("Enter Third Number: "))
    
    my_list = [num1, num2, num3]

    closest_num = min(my_list,key=lambda x:abs (x-target))

    print(f"The closest number to {target} is {closest_num}")
    return closest_num

find_closest_number()