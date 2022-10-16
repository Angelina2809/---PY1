money_capital = 10000 # финансовая подушка
salary = 5000 # зарплата
spend = 6000 #превышение расходов на проживание
increase = 0.05 # рост цен ежемесечно
pom=0
month = 0  # количество месяцев, которое можно прожить
while money_capital>0:
    if month==0:
        pom = spend
        money_capital = money_capital - pom
        month += 1

    else:
        spend = spend + spend * increase
        pom = spend - salary
        money_capital = money_capital - pom
        if money_capital>0:month += 1
print(month)
