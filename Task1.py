
def user_enter ():
    user_set1 = set()                        
    user_set2 = set()                       

    while True:
        try:
            user_count_set1 = int(input("Enter the count of first set: "))          
        except ValueError:
            print("Invalid input. Enter only an number: ")
            continue
        else: break

    while True:
        try:
            user_count_set2 = int(input("Enter the count of second set: "))          
        except ValueError:
            print("Invalid input. Enter only an number: ")
            continue
        else: break


    i = 0
    while i != user_count_set1:
        try:
            user_enter_set1 = float(input("Enter the element of first set: "))
            user_set1.add(user_enter_set1)
            i += 1
        except ValueError:
            print("Invalid input. Enter only an number: ")
            continue

    j = 0
    while j != user_count_set2:
        try:
            user_enter_set2 = float(input("Enter the element of second set: "))
            user_set2.add(user_enter_set2)
            j += 1
        except ValueError: 
            print("Invalid input. Enter only an number: ")
            continue
    
    return user_set1, user_set2


def join_set(sets):          
    result_list = sorted(list(sets[0] & sets[1]))
    return result_list

user_sets = user_enter()
result = join_set(user_sets)
print(f"Result: {result}")
