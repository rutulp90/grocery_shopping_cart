# Grocery Shopping Cart 🛒

A command-line interface (CLI) application built with Python to simulate a functional grocery shopping experience. This project was developed as part of the **GenAI & Agentic AI for Developers** program at IIT Patna (Module 0).

## 🚀 Features
* **Add Items:** Select and add grocery items with their prices to your cart.
* **Remove Items:** Delete unwanted items from your active shopping cart.
* **View Cart:** Display all current items in your cart along with their individual and total costs.
* **Checkout & Billing:** Finalize your order and generate a final receipt.
* **Robust Error Handling:** Uses `try-except` blocks and membership checks to prevent crashes from invalid inputs or missing items.

## 🛠️ Core Concepts Applied
* **Data Structures:** Utilized **Dictionaries** for storing store inventory (key-value pairs) and **Lists** for managing cart items.
* **Control Flow:** Implemented `while True` continuous loops with break conditions for interactive CLI navigation.
* **Conditional Logic:** Used `if-elif-else` statements to handle different user choices.
* **String Formatting & Methods:** Cleaned and formatted user input using `.strip()` and `.lower()`.
* **Functions:** Organized code into modular, reusable functions (`add_item`, `remove_item`, `view_cart`, etc.) to improve maintainability.

## 📂 Project Structure
```text
grocery-shopping-cart/
│
├── main.py           # Main application script
└── README.md         # Project documentation
