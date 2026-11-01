# Define the menu of cafe
menu={
    'burger':50,
    'pizza':100,
    'cold coffee':60,
    'plain fries':70,
}
# greet
print("Welcome To Piyuz Cafe")
print("burger:50\npizza:100\ncold coffee:60\nplain fries:70")

order_total=0
#30+70=100
dish_1=input("enter the name of your dish you want to order:")
if dish_1 in menu:
    order_total+=menu[dish_1]
    print(f"your dish {dish_1} has been added to your order")
else:
    print(f"ordered dish {dish_1} is not available")

another_order=input("Do you want to add another dish? (yes/no)")
if another_order=="yes":
    dish_2=input("enter the name of second dish:")
    if dish_2 in menu:
        order_total+=menu[dish_2]
        print(f"your dish {dish_2} has been added to your order")
    else:
        print(f"ordered dish {dish_2} is not available")

print(f"the total amount of dishes to pay is {order_total}")