list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_list=0
for index in range(len(list_numbers)):
    max_list1=list_numbers[max_list]
    cur_list=list_numbers[index]
    if cur_list>max_list1:
        max_list=index
list_numbers[max_list],list_numbers[-1]=list_numbers[-1],list_numbers[max_list]
# TODO Оформить решение

print(list_numbers)
