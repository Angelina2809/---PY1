from random import randint
def get_unique_list_numbers() -> list[int]:
    arr=[]
    mass = dict()
    number  = -10
    for i in range(21):
        mass[number] = True
        number+=1
    for i in range (16):
        cou = randint(-10, 10)
        if mass[cou]:
            arr.append(cou)
            mass[cou] = False
    return (arr)
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
