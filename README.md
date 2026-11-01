# Python Cafe Ordering System

## Project Overview

The **Python Cafe Ordering System** is a beginner-friendly, command-line
application that simulates a simple cafe ordering experience. Customers
can view the available menu, enter the name of a dish, choose whether to
add another item, and see the total amount to pay.

## Features

-   Displays the cafe menu with item prices.
-   Accepts a customer's dish selection.
-   Checks whether the selected dish is available.
-   Adds the price of valid dishes to the order total.
-   Allows the customer to add one more dish.
-   Calculates and displays the final bill.

## Menu

  Item            Price
  ------------- -------
  Burger             50
  Pizza             100
  Cold Coffee        60
  Plain Fries        70

## Python Concepts Used

-   **Dictionaries:** Store menu items and their prices.
-   **`input()`:** Collect dish selections and the customer's response.
-   **Conditional statements:** Check menu availability and whether
    another item should be added.
-   **Arithmetic operators:** Calculate the order total.
-   **Variables:** Keep track of the selected dishes and total amount.
-   **Formatted strings:** Display order confirmations and the final
    bill.

## How to Run

1.  Make sure Python is installed on your computer.
2.  Download or clone this repository.
3.  Open a terminal in the project folder.
4.  Run the script:

``` bash
python cafe_ordering.py
```

5.  Enter a dish name exactly as shown in the menu, such as `burger` or
    `cold coffee`.
6.  When prompted, enter `yes` to add another dish or `no` to finish.

## Sample Output

``` text
Welcome To Piyuz Cafe
burger:50
pizza:100
cold coffee:60
plain fries:70

enter the name of your dish you want to order: burger
your dish burger has been added to your order

Do you want to add another dish? (yes/no) yes
enter the name of second dish: pizza
your dish pizza has been added to your order

the total amount of dishes to pay is 150
```

## Possible Improvements

-   Allow customers to add more than two dishes.
-   Add quantity selection for each item.
-   Make menu selection case-insensitive.
-   Display an itemized bill.
-   Validate incorrect or empty inputs.

## Project Objective

This project demonstrates fundamental Python programming skills by
building a practical cafe ordering application using dictionaries, user
input, conditional logic, and basic calculations.

------------------------------------------------------------------------

**Project:** Python Cafe Ordering System\
**Language:** Python 3
