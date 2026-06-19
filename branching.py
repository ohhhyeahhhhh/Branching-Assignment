kw_hours = int(input("Enter the KW hours used: "))

Rate_Under_1000 = 0.07633
Rate_Over_1000 = 0.09259

if kw_hours <= 1000:
    amount_owed = kw_hours * Rate_Under_1000
else:

    amount_owed = (1000 * Rate_Under_1000) + ((kw_hours - 1000) * Rate_Over_1000)

print(f"Amount owed is ${amount_owed}")
