#question1:
"""
tests = ["Maths", "Science", "English", "IT"]
marks = [
    [80, 75, 90, 85],
    [70, 65, 95, 80],
    [60, 55, 100, 75],
    [50, 45, 85, 70],
    [40, 35, 75, 65],
    [30, 25, 65, 60],
    [20, 15, 55, 55],
    [10, 5, 45, 50],
    [5, 10, 35, 45],
    [0, 0, 25, 40]
]
total_marks = [sum(student_marks) for student_marks in marks]
highest_total= max(total_marks)
lowest_total = min(total_marks)
from statistics import mean
average_total = mean(total_marks)
print("the highest mark is", highest_total)
print("the lowest mark is", lowest_total)
print("the average mark is", average_total)

for i, test_marks in enumerate(zip(*marks)):
    highest_test = max(test_marks)
    lowest_test = min(test_marks)
    from statistics import mean
    average_test = mean(test_marks)
    print(f"For {tests[i]} test,the highest mark is {highest_test},)")
    print(f"For {tests[i]} test,the lowest mark is {lowest_test},)")
    print(f"For {tests[i]} test,the average mark is {average_test},)") 

    
#question2:
    
basic_salary = float(input("Enter the basic salary: "))
if basic_salary <= 10000:
    hra = basic_salary * 0.2
    da = basic_salary * 0.8 
elif basic_salary <= 20000:
    hra = basic_salary * 0.25 
    da = basic_salary * 0.9 
else:
    hra = basic_salary * 0.3 
    da = basic_salary * 0.95 
gross_salary = basic_salary + hra + da
print("The gross salary is: ", gross_salary)

#question 3
import re
def valid_password(password):
    if not re.search("[a-z]", password):
        return False   
    elif not re.search("[A-Z]", password):
        return False   
    elif not re.search("[0-9]", password):
        return False    
    elif not re.search("[$#@]", password):
        return False    
    elif len(password) < 6:
        return False   
    elif len(password) > 16:
        return False   
    else:
        return True
password = input("Enter your password: ")
if valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid. Please follow the specified criteria.")
    
#question4
lst= [10, 20, 30, 40, 50, 60, 70, 80]
lst.extend([200, 300])
lst.remove(10)
lst.remove(30)
lst.sort()
lst.sort(reverse=True)
print("Modified List list:", lst)

#question5
d= {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
d[6] = "Six"
d.pop(2, None)
key_6_present = 6 in d
print(f"Key 6 is{' ' if key_6_present else ' not '}present in d")
num_elements = len(d)
print(f"Number of elements in D: {num_elements}")
total_values_length = sum(len(value) for value in d.values())
print(f"Total length of all values in d: {total_values_length}")
 
 #question6
import random
random_numbers = [random.randint(100, 900) for _ in range(100)]
odd_numbers = [num for num in random_numbers if num % 2 != 0]
even_numbers = [num for num in random_numbers if num % 2 == 0]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [num for num in random_numbers if is_prime(num)]
print("Original List of 100 Random Numbers:", random_numbers)
print("(i) All Odd Numbers:", odd_numbers)
print("(ii) All Even Numbers:", even_numbers)
print("(iii) All Prime Numbers:", prime_numbers)
 
 #question 7
import interest 
principal = 2000
rate = 10
time = 3
interest = interest.compound_interest(principal, rate, time)
print(f"The compound interest for {principal} at {rate}% for {time} years is {interest}")"""

 #question8
#a
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name + " serves " + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name + " is open now.")

restaurant = Restaurant("Pizza Hut", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#b

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = ""
        self.username = ""
        self.password = ""
        self.bio = ""
    
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"Bio: {self.bio}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our website.")

user1 = User("Manali", "Sarna")
user2 = User("Kunal", "Jain")
user3 = User("Kiara", "Barar")

user1.email = "manali@gmail.com"
user1.username = "dhruv"
user1.password = "password1"
user1.bio = "I love Pancake!"

user2.email = "kunal@yahoo.com"
user2.username = "kunal"
user2.password = "password2"
user2.bio = "I love meggi!"

user3.email = "kiara@outlook.com"
user3.username = "kiara"
user3.password = "password3"
user3.bio = "I love chai!"

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
