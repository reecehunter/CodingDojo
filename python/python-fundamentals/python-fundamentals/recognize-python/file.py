num1 = 42 # variable declaration - initialize int
num2 = 2.3 # variable declaration - initialize float
boolean = True # variable declaration - initialize boolean
string = 'Hello World' # variable declaration - initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration - initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration - initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration - initialize tuple
print(type(fruit)) # type check
print(pizza_toppings[1]) # list - access value
pizza_toppings.append('Mushrooms') # list - add value
print(person['name']) # list - access value
person['name'] = 'George' # list - change value
person['eye_color'] = 'blue' # list - change value
print(fruit[2]) # list - access value

if num1 > 45: # conditional - if
    print("It's greater")
else:  # conditional - else
    print("It's lower")

if len(string) < 5:  # conditional - if
    print("It's a short word!")
elif len(string) > 15:  # conditional - else if
    print("It's a long word!")
else: # conditional - else
    print("Just right!")

for x in range(5): # for loop - start
    print(x)
for x in range(2,5):  # for loop - start
    print(x)
for x in range(2,10,3):  # for loop - start
    print(x)
x = 0  # variable declaration - initialize int
while(x < 5): # while loop - start
    print(x)
    x += 1

pizza_toppings.pop() # list - delete value
pizza_toppings.pop(1) # list - delete value with paramter

print(person)
person.pop('eye_color') # list - delete value
print(person)

for topping in pizza_toppings: # for loop - start
    if topping == 'Pepperoni': # conditional - if
        continue
    print('After 1st if statement')
    if topping == 'Olives': # conditional - if
        break # for loop - break

def print_hello_ten_times(): # function declaration
    for num in range(10): # for loop - start
        print('Hello')

print_hello_ten_times() # function call

def print_hello_x_times(x): # function declaration
    for num in range(x): # for loop - start
        print('Hello')

print_hello_x_times(4) # function call

def print_hello_x_or_ten_times(x = 10): # function declaration
    for num in range(x): # for loop - start
        print('Hello')

print_hello_x_or_ten_times() # function call
print_hello_x_or_ten_times(4) # function call, function paramater


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)