from pyscript import document, display

name = 'Carlos David' # string
age = 14 # integer
height1 = 171 # integer
dream_countries = ['USA', 'United Kingdom', 'Italy'] # list
country1 = dream_countries[0] # indexing of 1st item in list
country2 = dream_countries[1] # indexing of 2nd item in list
country3 = dream_countries[2] # indexing of 3rd item in list

student_type = False # boolean

additional_info = {
    'color': 'White',
    'car_brand': 'Lamborghini',
    'shoe_size': 10.5,
    'best_friend': 'ACM'
} # dictionary

fruits = {'grapes', 'strawberry', 'mango', 'kiwi', 'watermelon'} # set
days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') # tuple


# Displaying the Information using display()
display(f'Name: {name}', target="about-output")
display(f'Age: {age}', target="about-output")
display(f'Height: {height1} cm', target="about-output")
display(f'Dream Countries: {country1}, {country2}, {country3}', target="about-output")
display(f'New Student: {student_type}', target="about-output")
display(f'Favorite Color: {additional_info["color"]}', target="about-output")
display(f'Favorite Car Brand: {additional_info["car_brand"]}', target="about-output")
display(f'Shoe Size: US {additional_info["shoe_size"]}', target="about-output")
display(f'Best Friends: {additional_info["best_friend"]}', target="about-output")


# Operators for Calculator

def adding_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    # Gets sum when num1 is added with num2
    result = num1 + num2
    display(f'Result: {result}', target="output1")


def subtracting_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    # Gets difference when num1 is subtracted by num2
    result = num1 - num2
    display(f'Result: {result}', target="output1")


def multiplying_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    # Gets product when num1 is multiplied by num2
    result = num1 * num2
    display(f'Result: {result}', target="output1")


def dividing_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    # Gets quotient when num1 is divided by num2
    result = num1 / num2
    display(f'Result: {result}', target="output1")


def modulo_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    # Gets remainder when num1 is divided by num2
    result = num1 % num2
    display(f"Result: {result}", target="output1")