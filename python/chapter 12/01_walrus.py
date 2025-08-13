# 📌 The walrus operator (:=) allows you to assign a value to a variable within an expression.
# It was introduced in Python 3.8.

# 🧠 Why use it? To make code shorter and avoid repeating calculations like len(), input(), etc.

# 👇 Example: Checking if a list is too long using the walrus operator

# Let's say this is our data (e.g., submitted by a user)
user_data = [10, 20, 30, 40, 50]  # This list has 5 items

# 🟡 Without walrus operator, you'd typically write:
# n = len(user_data)
# if n > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")

# ✅ Now using the walrus operator:
if (n := len(user_data)) > 3:
    # Here, `n` is assigned the value of len(user_data), and we immediately check if it's > 3
    print(f"List is too long ({n} elements, expected <= 3)")
else:
    print("List length is acceptable.")
