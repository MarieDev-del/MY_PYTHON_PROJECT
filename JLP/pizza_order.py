#Pizza order program; amount is in Rs
 #Small pizza = 100
 #Medium pizza = 200
 #Large pizza = 300
 
#pepperoni for small pizza  = 30
#pepperoni for small pizza  = 50
#pepperoni for small pizza  = 50

#Extra cheese for any size pizza = 20

pizza_size = input("Enter the pizza size you want,L/M/S: ")
bill = 0

if pizza_size == "s" or pizza_size == "S":
    bill += 100
    print(f"{pizza_size.upper()} size is 100Rs")
elif pizza_size == "m" or pizza_size == "M":
    bill += 200
    print(f"{pizza_size.upper()} size is 200Rs")
else:
    bill += 300
    print(f"{pizza_size.upper()} size is 500Rs")
    
add_pepperoni = input("Do you want to add pepperoni,Yes/No? ")
if add_pepperoni == "Yes" or add_pepperoni == "yes":
    if pizza_size == "s" or pizza_size == "S":
        bill += 30
        print("Pepperoni for small size pizza is 30Rs")
    else:
        bill += 50
        print(f"Pepperoni for {pizza_size.upper()} size pizza is 50Rs")
extra_cheese = input("Do you want extra cheese,Yes/No? ")
if extra_cheese == "Yes" or extra_cheese == "yes":
    bill += 20
    print("Extra cheese cost 20Rs for any pizza size")

print(f"Total bill is {bill}\nThanks for your patronage")