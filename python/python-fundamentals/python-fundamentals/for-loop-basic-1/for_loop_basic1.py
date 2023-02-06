for i in range(151):
    print(i)

for i in range(1001):
    if(i % 5 == 0):
        print(i)

for i in range(1, 101):
    if(i % 10 == 0):
        print("Dojo")
    elif(i % 5 == 0):
        print("Coding")

sum = 0
for i in range(500000):
    if(i % 2 != 0):
        sum += i
print(sum)

for i in range(2018, 0, -4):
    if(i >= 0):
        print(i)

low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
    if(i % mult == 0):
        print(i)