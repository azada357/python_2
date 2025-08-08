print("hello")
print("*"*10)
x = input("x : ")
y = int(x) +1
print(y)
age = 21
if age >= 18 and age <=25:
    print("eligible")
for number in range(4):
    print("message")
    print((number + 1) *7)
successful = False
for number in range(3):
   print("attempt")
   if successful:
       print("successful")
       break
else:
    print("3 times attempted and failed")
for x in range(4):
    for y in range(2):
        print(f"({x},{y})")
number = 100
while number > 0:
    print(number)
    number//=2
else:
    print("done")
command = ""
while command != "Exit":
    command = input(">>>")
    print(command)
else:
    print("done")
countdown = 3
while countdown > 0:
    print("Hello")
    countdown -=1
else:
    print("countdown is complete")
time = 45
while time <60:
    print("Keep going")
    time +=1
    
else:
    print("you are done")
counter = 1
sum = 0
while counter <= 100:
    sum += counter
    counter +=2
print(sum)
print("Done!")
counter = 1
sum = 0
while counter <= 3:
    sum+=counter
    counter += 1
print(sum)
x = 10
while x > 5:
    print(x)
    x -= 2
count = 5
while count>0:
    print("hello")
    count -= 1
count = 10
while count >0:
    print(count)
    count -=1
print("liftoff")
counter = 1
sum = 0
while counter<= 200:
    sum += counter
    counter += 2
print(sum)
x = 100

while x > 0:
    x -= 5
    print("feul remaining", x)
print("out of feul")
    
def get_greet(First_name):
    return f"hi{First_name}"
message = get_greet(" Azada")
file = open("content.txt", "w")
file.write(message)

def bring(Do_verb):
    print(f"{Do_verb}learn python")
bring("deos")
def Devide_two_numbers(original_number, devide_number):
    return original_number/ devide_number
number_1 = 8
number_2 = 4
print(Devide_two_numbers(number_1, number_2))

def Modify_number(original_number, devide_number):
    original_number = original_number/ devide_number
number_1 = 7
number_2 = 5
number_1 = Modify_number(number_1, number_2)
print(number_1)
name = input ("what is your name?")
print("hello" +name)
def divide(a, b):
    return a / b
print(divide(10,2))


Print("Hello World")