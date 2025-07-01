# ☕ Coffee Machine Program

A simple console-based Coffee Machine simulation written in Python. This program allows users to choose between espresso, latte, and cappuccino, checks for ingredient availability, processes coin-based payments, and updates resources accordingly.

---

## 📋 Features

- Choose your drink: `espresso`, `latte`, or `cappuccino`
- Ingredient availability check before processing the order
- Coin-based payment system (quarters, dimes, nickels, pennies)
- Automatic calculation of total payment and change
- Displays machine resource report
- Maintainer mode to shut down the machine using `off`

---

## 🚀 How It Works

1. Run the program.
2. You’ll be prompted with:
   ```
   Type in Your Drink Name:
   1.Espresso
   2.Latte
   3.Cappuccino
   ```
3. Type your choice (e.g., `latte`)
4. If enough resources are available, insert coins as prompted
5. If payment is successful:
   - Coffee is made ☕
   - Ingredients are deducted
   - Change (if any) is returned
6. Type `report` to see remaining resources
7. Type `off` to turn off the machine

---

## 🛠 Requirements

- Python 3.x

---

## 📁 Project Structure

```
.
├── main.py         # Main Coffee Machine code (your finalized code)
└── kitchen.py      # Contains MENU and resources dictionaries
```

**`kitchen.py` example:**
```python
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

---

## ✅ Sample Output

```
Type in Your Drink Name:
1.Espresso
2.Latte
3.cappuccino
latte
Insert Quarters($0.25): 10
Insert dimes($0.10): 0
Insert nickles($0.05): 0
Insert pennies($0.01): 0
Here is your latte, Enjoy!
Here is your change: $0.0
```

---

## 📌 Notes

- All input is case-insensitive.
- Outputs are formatted for clarity.
- Great beginner project to understand functions, conditionals, loops, and dictionaries in Python.

---


Made with 💙 by ashahmir

