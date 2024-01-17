# Calculating highest score from given scores

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score >= highest_score:
#     highest_score = score
# print(f"The highest score is {highest_score}")    

# FizzBuzz game
# target = 100
# for n in range(1,target + 1):
#     if  n % 3 and n % 5 == 0:
#         print("FizzBuzz") 
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)           

# Password Generator Project
import random 
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char

for char in range(1,nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1,nr_symbols + 1):
    password += random.choice(symbols)

print(password)        