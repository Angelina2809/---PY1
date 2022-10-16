salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
pom=0
for i in range(months):
    if i == 0:
        pom=spend-salary
        need_money=need_money+pom
    else:
        spend = spend + spend * increase
        pom = spend - salary
        need_money = need_money+pom
print(round(need_money))
