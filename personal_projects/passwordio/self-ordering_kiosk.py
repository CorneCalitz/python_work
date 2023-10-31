"""Python algorithm for a self-ordering kiosk operated by robots"""

menu = [
    {"name": "Fish and chips",
     "status": "available",
     "ingredients_used": [
         {"name": "fish", "used": 1},
         {"name": "potato", "used": 2}
     ]
     },
    {"name": "Hamburger",
     "status": "available",
     "ingredients_used": [
         {"name": "patty", "used": 1},
         {"name": "bun", "used": 1}
     ]
     },
    {"name": "Hot dog",
     "status": "available",
     "ingredients_used": [
         {"name": "sausage", "used": 1},
         {"name": "bread roll", "used": 1}
     ]
     }
]

stock_ingredients = [
    {"name": "fish", "amount": 1},
    {"name": "potato", "amount": 2},
    {"name": "bun", "amount": 4},
    {"name": "bread roll", "amount": 4},
    {"name": "patty", "amount": 4},
    {"name": "sausage", "amount": 4},
]

order_db = []
order_list = []

# ------- Start of algorithm ------------

# Step 1: Display menu and get response
i = 0
print("---Menu---")
for items in menu:
    if items["status"] == "available":
        i += 1
        print(i, items["name"])

customer_order = int(input("Input order number: ")) - 1

# Step 2: Subtract order ingredients with in stock ingredients
print("\nCooking food. Please wait patiently.")

ingredients_used = menu[customer_order]["ingredients_used"]

for ingredient_used in ingredients_used:

    for stock_ingredient in stock_ingredients:

        if ingredient_used["name"] == stock_ingredient["name"]:
            stock_ingredient["amount"] = stock_ingredient["amount"] - ingredient_used["used"]
            print(ingredient_used["name"].title(), "is ready")

# Step 3: Serve food, save order to db and clear customer order
print("Food is ready. Here is your", menu[customer_order]["name"])

order_db.append(menu[customer_order]["name"])

customer_order = ""

# Step 4: Make a menu item unavailable if ingredients are not in stock and ingredients to supplier order list.
for stock_ingredient in stock_ingredients:
    if stock_ingredient["amount"] <= 0:
        order_list.append(stock_ingredient["name"])

        for item in menu:
            items_used = item["ingredients_used"]
            for item_used in items_used:
                if stock_ingredient["name"] == item_used["name"]:
                    item["status"] = "unavailable"

print("Item(s) to order: ", order_list)

print("\n---Menu updated---")
i = 0
for items in menu:
    if items["status"] == "available":
        i += 1
        print(i, items["name"])