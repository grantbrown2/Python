print("------ This is the answer for question 1 ------")
for i in range(151):
    print(i)


print("------ This is the answer for question 2 ------")
for x in range(5,1005,5):
    print(x)


print("------ This is the answer for question 3 ------")
for y in range(101):
    if y % 10 == 0:
        print("Coding Dojo")
    elif y % 5 == 0:
        print("Coding")
    else:
        print(y)

sum = 0
for odd in range(1, 500001, 2):
    sum += odd
print("------ This is the answer for question 4 ------")
print(sum)

print("------ This is the answer for question 5 ------")
for countdown in range(2018, 0, -4):
    print(countdown)

print("------ This is the answer for question 6 ------")
lowNum = 0
highNum = 12
mult = 2
for v in range(lowNum,highNum, + 1):
    if v % mult == 0:
        print(v)