import random

start_price = 100
current_price = start_price
price_history = [current_price]

num_days = 252

for day in range(num_days):
    direction = random.choice([-1, 1])
    change = direction * random.uniform(0, 2)
    current_price += change
    price_history.append(current_price)

print(f"starting price: {start_price}")
print(f"Final price after {num_days} days: {current_price}")
print(
    f"Highest price reached {max(price_history)} and the lowest price is {min(price_history)}")
