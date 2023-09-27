
def user_enter():
    array_of_berries = []
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
            array_of_berries.append(count_of_berries)
            i += 1
            if len(array_of_berries) == count_of_bush: break
            else: continue

    return array_of_berries



def result(array_of_berries):
    
    print(array_of_berries)
    
    result = []
    result.append(array_of_berries[-1] + array_of_berries[0] + array_of_berries[1])

    for i in range(len(array_of_berries[1:-1])):
        result.append(array_of_berries[i+1] + array_of_berries[i] + array_of_berries[i+2])

    result.append(array_of_berries[0] + array_of_berries[-1] + array_of_berries[-2])
    
    return result


array_of_berries = user_enter()
print(f"Result: {result(array_of_berries)}")
