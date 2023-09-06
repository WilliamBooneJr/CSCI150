#William Boone
#Assignment 4 food receipt

food1 = input('Enter food item name:' )
print(food1)

food1price = float(input('Enter item price:' ))
print(f'{food1price:.2f}')

food1qnt = int(input('Enter item quantity:' ))
print(food1qnt)

food2 = input('Enter second food item name:' )
print(food2)

food2price = float(input('Enter item price:' ))
print(f"{food2price:.2f}")

food2qnt = int(input('Enter item quantity:' ))
print(food2qnt)

food1sum = food1qnt * food1price
food2sum = food2qnt * food2price
total_cost = food1sum + food2sum

print('Order Receipt')
print(f"{food1qnt} {food1} {'@'} {'$'}{food1price} {'='} {'$'}{food1sum:.2f}")
print(f"{food2qnt} {food1} {'@'} {'$'}{food2price} {'='} {'$'}{food2sum:.2f}")
print(f"{'Total cost:'} {'$'}{total_cost:.2f}")

_gratuity = .15 * total_cost
totaltip = total_cost + _gratuity

print(f"{'15% gratuity:'} {'$'}{_gratuity:.2f}")
print(f"{'Total with tip:'} {'$'}{totaltip:.2f}")




