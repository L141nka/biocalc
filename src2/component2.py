#моделювання розмноження клітин

#1 поділ приблизно за 20 хв

#початкова кількість бактерій
def bacteriaAmount(start_amount):
    rate = int(t/cycle)

    for i in range(rate):
        start_amount *= 2

    return f"Кількість бактерій після {int(t/60)} годин: {'{:.2e}'.format(start_amount)}"
    
cycle = 20 #час в хв за який культура ділиться
start_amount = int(input("Введіть кількість бактерій (в од.): "))
t = int(input("Введіть час розмноження культури (в год): ")) * 60

result_amount_bacteria = bacteriaAmount(start_amount)

print(result_amount_bacteria)


