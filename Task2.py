
def user_enter():
    array_of_berriesay_of_berries = []
    i = 1
    while True: 
        try: count_of_bush = int(input("Enter the count of bush: "))
        except ValueError: 
            print("Invalid input. Enter only an integer.")
            continue
        else: break

    while True:
        try: count_of_berries = int(input(f"Enter the count of berries on {i} bush: "))
        except ValueError:
            print("Invalid input. Enter only an integer.")
            continue
        else: 
            array_of_berriesay_of_berries.append(count_of_berries)
            i += 1
            if len(array_of_berriesay_of_berries) == count_of_bush: break
            else: continue

    while True:
        try: number_of_bush = int(input("Enter the number of the bush you want to start with(central): "))
        except ValueError:
            print("Invalid input. Enter only an integer.")
            continue
        else: break

    return array_of_berriesay_of_berries, number_of_bush


def result(array_of_berries, number_of_bush):
    
    print(array_of_berries)
    
    result = 0
    if number_of_bush == 1:
        result = array_of_berries[0] + array_of_berries[1] + array_of_berries[-1]
    elif number_of_bush == len(array_of_berries):
        result = array_of_berries[-2] + array_of_berries[-1] + array_of_berries[0]
    else:
        result = array_of_berries[number_of_bush - 1] + array_of_berries[number_of_bush - 2] + array_of_berries[number_of_bush]
    
    return result


array_of_berries = user_enter()
print(f"Result: {result(array_of_berries[0], array_of_berries[1])}")
