"""
Ex. No. 2 - Electricity Billing System Using Conditional Statements and Loops

Aim:
    To develop a Python-based electricity billing system that calculates
    energy consumption charges using slab rates, conditional statements
    and loops.

Slab rates used:
    First 100 units      : Rs. 1.50 per unit
    Next 100 units       : Rs. 2.50 per unit
    Next 300 units       : Rs. 4.00 per unit
    Above 500 units      : Rs. 6.00 per unit
"""


def calculate_bill(units):
    """Return the bill amount for the given units, calculated slab by slab."""
    bill = 0
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00
    return bill


# Read the number of customers
n = int(input("Enter number of customers: "))

# Repeat the billing process for every customer
for i in range(1, n + 1):
    print(f"\nCustomer {i}")
    name = input("Enter customer name: ")
    units = float(input("Enter units consumed: "))
    bill = calculate_bill(units)
    print("Customer Name :", name)
    print("Units         :", units)
    print("Bill Amount   : Rs.", round(bill, 2))
