number = int (input("Enter an amount of money (divisible by 1000): "))
first_coin = number // 5000
second_coin = (number - first_coin * 5000) // 2000
third_coin = (number - first_coin * 5000 - second_coin * 2000) // 1000
print(number,"= [", first_coin,"]*5000 +","[", second_coin, "]*2000 +", "[", third_coin, "]" "*1000")
# second way
print(f"{number} = [{first_coin}]*5000 + [{second_coin}]*2000 + [{third_coin}]*1000")

# third way
number = int(input("Enter an amount of money (divisible by 1000): "))

# Calculate number of 5000 coins
first_coin = number // 5000
remainder = number % 5000

# Calculate number of 2000 coins
second_coin = remainder // 2000
remainder %= 2000

# Calculate number of 1000 coins
third_coin = remainder // 1000

# Print result
print(f"{number} = [{first_coin}]*5000 + [{second_coin}]*2000 + [{third_coin}]*1000")
