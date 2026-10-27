<<<<<<< HEAD

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]


total_cost = 0
for product in products:
    total_cost += product["price"] * product["quantity"]


def apply_discount(total):
    if total >= 2000:
        return total * 0.90  
    return total

final_price = apply_discount(total_cost)

print(f"Total Cart Cost: BDT {total_cost:.2f}")
=======

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]


total_cost = 0
for product in products:
    total_cost += product["price"] * product["quantity"]


def apply_discount(total):
    if total >= 2000:
        return total * 0.90  
    return total

final_price = apply_discount(total_cost)

print(f"Total Cart Cost: BDT {total_cost:.2f}")
>>>>>>> e9f3b641592de2382b358d3f06bfd1fc013d08ba
print(f"Final Payable Amount: BDT {final_price:.2f}")