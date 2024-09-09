kilowatts = int(input("Enter the KW hours used\n"))
rate1 = 7.633
rate2 = 9.259
if kilowatts <= 1000:
    cents = kilowatts * rate1
elif kilowatts > 1000:
    cents = 1000 * rate1 + (kilowatts - 1000) * rate2

money = cents/100

print(f"Amount owed is $",round(money, 2))


