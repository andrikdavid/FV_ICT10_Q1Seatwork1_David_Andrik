from pyscript import document, display

name = 'Carlos David' # string
age = 14 # integer
height1 = 171 # integer
dream_countries = ['USA', 'United Kingdom', 'Italy'] # list
country1 = dream_countries[0]
country2 = dream_countries[1]
country3 = dream_countries[2]

student_type = False # boolean

additional_info = {
    'color': 'White',
    'car_brand': 'Lamborghini',
    'shoe_size': 10.5,
    'best_friend': 'ACM'
} # dictionary

fruits = {'grapes', 'strawberry', 'mango', 'kiwi', 'watermelon'} # set
days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') # tuple



display(f'Name: {name}')
display(f'Age: {age}')
display(f'Height: {height1}cm')
display(f'Dream Countries: {country1}, {country2}, {country3}')
display(f'New Student: {student_type}')
display(f'Favorite Color: {additional_info['color']}')
display(f'Favorite Car Brand: {additional_info['car_brand']}')
display(f'Shoe Size: US {additional_info['shoe_size']}')
display(f'Best Friends: {additional_info['best_friend']}')


def adding_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    result = num1 + num2
    display(result, target="output1")


def subtracting_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    result = num1 - num2
    display(result, target="output1")


def multiplying_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    result = num1 * num2
    display(result, target="output1")


def dividing_numbers(e):
    document.getElementById("output1").innerHTML = ""

    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    result = num1 // num2
    display(result, target="output1")

