src = not False and True or False and not True
# src=True and True or False and False # избавляемся от отрицания
# src=True or False # избавляемся от логического И
# src=True # избавляемся от логического ИЛИ
# TODO расписать упрощение выражения

result = True  # TODO подставить результат выражения

print(src == result)
