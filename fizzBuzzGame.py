# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit + " Pie")
# print(fruits)

# total = 0
# for number in range(1, 11):
#     total += number
# print(total)
    
### Print out Even number between one and input range
# target = int(input('Number'))
# for number in range(2, target + 1, 2):
#     print(number)
    
# target1 = int(input('Number'))
# for number in range(2, target1 + 1, 2):
#     target1 += number
#     print(number)

### Fizz Buzz Game
### If Divide by 3 = Fizz
### If Divide by 5 = Buzz
### If Divide by 3 and 5 = FizzBuzz

number = 0
for num in range(1, 101):
    if num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    else: 
        print(num)
        