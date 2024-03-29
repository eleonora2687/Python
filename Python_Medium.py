#Right Shift by Division

##def shift_to_right(x, y):
##    return x//2**y
##
##
##print(shift_to_right(80, 3))
##print(shift_to_right(-24, 2))
##print(shift_to_right(-5, 1))
##print(shift_to_right(4666, 6))
##print(shift_to_right(3777, 6))
##print(shift_to_right(-512, 10))


#Find the Highest Integer in the List Using Recursion

##def find_highest(lst):
##    if len(lst)==1:
##        return lst[0]
##    else:
##        if lst[len(lst)-1]<lst[len(lst)-2]:
##            lst.remove(lst[len(lst)-1])
##        else:
##            lst.remove(lst[len(lst)-2])
##        return find_highest(lst)
##
##print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
##print(find_highest([0, 12, 4, 87]))
##print(find_highest([8]))

##Length of Number

##def number_length(num):
##    if num==0:
##        return 1
##    else:
##        counter=0
##        while num>0:
##            num//=10
##            counter+=1
##        return counter
##
##print(number_length(10))
##print(number_length(5000))
##print(number_length(0))
##

##FizzBuzz Interview Question

##def fizz_buzz(num):
##    if num%3==0 and num%5==0:
##        return "FizzBuzz"
##    elif num%3==0:
##        return "Fizz"
##    elif num%5==0:
##        return "Buzz"
##    return str(num)
##
##print(fizz_buzz(3))
##print(fizz_buzz(5))
##print(fizz_buzz(15))
##print(fizz_buzz(4))


##Geometry 1: Length of Line Segment

##import math
##def line_length(dot1, dot2):
##    return round(math.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2),2)
##
##print(line_length([15, 7], [22, 11]))
##
##print(line_length([0, 0], [0, 0]))
##
##print(line_length([0, 0], [1, 1]))



##Sum of Odd and Even Numbers

##def sum_odd_and_even(lst):
##    my_list=[]
##    sum_odd=0
##    sum_even=0
##    for i in range(len(lst)):
##        if lst[i]%2==0:
##            sum_even+=lst[i]
##        else:
##            sum_odd+=lst[i]
##    
##    my_list.append(sum_even)
##    my_list.append(sum_odd)
##    return my_list
##
##print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
##print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
##print(sum_odd_and_even([0, 0]))


##Cricket Balls to Overs!

##def total_overs(balls):
##    quotient=balls//6
##    remainder=balls%6
##    if remainder==0:
##        return quotient
##    return quotient+remainder/10
##    
##
##print(total_overs(2400))
##
##print(total_overs(164))
##print(total_overs(945))
##print(total_overs(5))


##Burglary Series (03): Is It Gone?

##def find_it(items, name):
##    if items.get(name) is not None:
##        return name.capitalize()+" is gone..."
##    return name.capitalize()+" is here!"
##
##print(find_it({"tv": 30,"timmy": 20,"stereo": 50,},"timmy"))
##
##print(find_it({"tv": 30,
##  "stereo": 50,
##},"timmy"))
##
##print(find_it({},"timmy"))


##A Circle and Two Squares

##def square_areas_difference(r):
##    return 2*r**2
##
##print(square_areas_difference(5))
##
##print(square_areas_difference(6))
##
##print(square_areas_difference(7))


##Get Students with Names and Top Notes

##def top_note(student):
##    my_dict=student.copy()
##    my_dict["top_note"]=my_dict.pop("notes")
##    my_dict.update({"top_note": max(my_dict.get("top_note"))})
##    return my_dict
##
##print(top_note({ "name": "John", "notes": [3, 5, 4] }))
##
##print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
##
##print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))


##Calculate the Profit

##import math
##def profit(info):
##    return round(info.get("inventory")*(info.get("sell_price")-info.get("cost_price")))
##
##
##print(profit({
##  "cost_price": 32.67,
##  "sell_price": 45.00,
##  "inventory": 1200
##}))
##
##print(profit({
##   "cost_price": 225.89,
##  "sell_price": 550.00,
##  "inventory": 100
##}))
##
##print(profit({
##   "cost_price": 2.77,
##  "sell_price": 7.95,
##  "inventory": 8500
##}))


##Get the Area of a Country

##def area_of_country(name, area):
##    return "{} is {}% of the total world's landmass".format(name,round((area/148940000)*100,2))
##
##print(area_of_country("Russia", 17098242))
##print(area_of_country("USA", 9372610))
##print(area_of_country("Iran", 1648195))


##Next Number Greater Than A and B and Divisible by B

##def divisible_by_b(a, b):
##    while True:
##        if a%b==0:
##            break
##        a+=1
##    return a
##
##print(divisible_by_b(17, 8))
##
##print(divisible_by_b(98, 3))
##
##print(divisible_by_b(14, 11))


##Next Number Greater Than A and B and Divisible by B Using Recursion

##def divisible_by_b(a, b):
##    if a%b==0:
##        return a
##    return divisible_by_b(a+1, b)
##
##print(divisible_by_b(17, 8))
##
##print(divisible_by_b(98, 3))
##
##print(divisible_by_b(14, 11))


##How Many Solutions Does This Quadratic Have?

##def solutions(a, b, c):
##    if b**2-4*a*c==0:
##        return 1
##    return (2 if b**2-4*a*c >0 else 0)
##
##print(solutions(1, 0, -1))
##
##print(solutions(1, 0, 0))
##
##print(solutions(1, 0, 1))


##Date Format

##def format_date(date):
##    s=''
##    for i in range(6,10):
##        s+=date[i]
##    for i in range(3,5):
##        s+=date[i]
##    for i in range(0,2):
##        s+=date[i]
##    return s
##
##print(format_date("11/12/2019"))
##    
##print(format_date("12/31/2019"))
##
##print(format_date("01/15/2019"))
##    


##Adding Numbers

##def add(n1, n2):
##    if n1=="" or n2=="" or n1==None or n2==None:
##        return "Invalid Operation"
##    x=int(n1)
##    y=int(n2)
##    return str(x+y)
##
##print(add("111", "111"))
##print(add("10", "80"))
##print(add("", "20"))


##List of Multiples

##def list_of_multiples (num, length):
##    lst=[]
##    for i in range(length):
##        lst.append(num*(i+1))
##    return lst
##
##print(list_of_multiples(7, 5))
##
##print(list_of_multiples(12, 10))
##
##print(list_of_multiples(17, 6))
##



##Quadratic Equation

##import math
##def quadratic_equation(a, b, c):
##    return (int)((-b+math.sqrt(b**2-4*a*c))/(2*a))
##
##print(quadratic_equation(1, 2, -3))
##
##print(quadratic_equation(2, -7, 3))
##
##print(quadratic_equation(1, -12, -28))



##Simple OOP Calculator

class Calculator:
    def add(self,num1,num2):
        return num2+num1
    def subtract(self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        return num1/num2

calculator = Calculator()

print(calculator.add(10,5))

print(calculator.subtract(10, 5))

print(calculator.multiply(10, 5))

print(calculator.divide(10, 5))






























































































































































































































