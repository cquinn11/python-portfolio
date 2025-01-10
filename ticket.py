#Charlotte Quinn
#12/12/2024

#Initialize
import turtle
t = turtle.Turtle()

#Functions
#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket

    
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")


#Main
print("Welcome to the ticket store!")
name = input("Please enter your name:")
age = int(input("Enter your age:"))
day = input("Day of the week today:")
code = input("coupon code('none' if no coupon code):")
                 
price = 100
if age <= 3 or age <3:
        price = 0 #price is 0 for babies
elif 4<age<17:
    if day == "saturday" or day == "sunday":
            price = 100
    else:
            price = 50
elif age >= 4 and day == "sunday" and code == "SUNDAYFUNDAY":
        price = 85
elif code == "none":
        price == price
elif age == 18 or age>18:
        price = 100
    
draw_ticket(name, price, day, 10)

