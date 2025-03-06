'''
Q1:

Write a Python function categorize_temperature(temp) that takes the temperature in Celsius as input and returns "Cold" if the temperature is below 10, "Warm" if it is between 10 and 25, and "Hot" if it is above 25.

'''

def categorize_temperature(temp: int): #take temp in celcius
    if temp < 10:
        return f"Cold"
    
    if temp >= 10 and temp <= 25:
        return f"Warm"
    
    if temp > 25:
        return f"Hot"




'''
Q2:

Write a Python function analyze_ratings(ratings) that takes a list of customer ratings (integers from 1 to 5) and returns another list containing the highest and lowest rating. 

'''

def analyze_ratings(ratings: list):
    m = 0
    l = 10
    for item in ratings:
        if m<item:
            m = item

        if l>item:
            l = item
    result = [m, l]

    return result


'''
Q3:

Write a Python function print_multiplication_table(number, range_limit) that takes a number and a range limit as input, and prints the multiplication table for the given number up to the specified range.

'''
def print_multiplication_table(number: int, range_limit: int):
    for i in range(1, range_limit+1):
        print(f"{number}x{i} = {number*i}")


    return

'''
Q4:

Write a Python function print_student_averages(grades) that takes a 2D list where each inner list represents a student's grades in different subjects. The function should print each student's grades and their average grade. 

'''

def print_student_average(grades: list):
    count = 1
    for std_grades in grades:
        add = 0
        for sub in std_grades:
            add += sub
        print(f"Student {count} grades: {std_grades}, avg {add/len(std_grades)}")
        count+=1

    return



#Q1 call

user_input1 = 15
print(categorize_temperature(user_input1))

#Q2 Call

user_input2 = [2,3,4,1,5,2,3]
print(analyze_ratings(user_input2))

#Q3 call
 
num = 5
r = 10
print_multiplication_table(num, r)

#Q4 call

grades = [[50, 60, 70, 80], [80, 75, 89, 90], [67,89,58,76]]

print_student_average(grades)