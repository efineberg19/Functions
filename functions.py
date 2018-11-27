#!/ysr/bin/python
#functions.py

'''Functions that users choose and play by giving input'''

__author__ = "Beth Fineberg"
__version__ = "1.0"

import turtle
import random
import time
import math

def draw_polygon(number_of_sides, side_length, t, win):
    t.speed(5)
    turtle.colormode(255)
    #pick random color
    t.fillcolor((random.randrange(0, 257, 10), random.randrange(0, 257, 10), 
                 random.randrange(0, 257, 10)))
    
    #draws polygon and fills in w/ color
    t.begin_fill()    
    for i in range(number_of_sides):
        t.forward(side_length)
        t.right(360 / number_of_sides) 
    t.end_fill()
    
    time.sleep(1)
    
def random_polygons(number_of_polygons, t, win):
    win.reset()
    for i in range(number_of_polygons):
        t.penup()
        
        t.goto(int(random.randrange(-200, 200)), 
               int(random.randrange(-200, 200)))
        
        #draws polygon using other function
        t.pendown()          
        draw_polygon(int(random.randrange(3, 20)), 
                     int(random.randrange(10, 90)), t, win)
        
    time.sleep(2)

def draw_stairs(number_of_stairs, t, win):
    win.reset()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    
    num_stairs = number_of_stairs + 1
    
    #draws stairs
    t.begin_fill()
    for stair in range(num_stairs):
        t.forward(400 / num_stairs)
        t.left(90)
        t.forward(400 / num_stairs)
        t.right(90)
        
    #completes stairs
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(400)  
    
    t.end_fill()
    time.sleep(2)
    
def should_answer_cell(is_morning, is_mom, is_asleep):
    '''determines if user should answer their cell phone depending on conditions
    :param is_morning: True if time is morning, False if not
    :param is_mom: True if mother is calling, False if not
    :param is_asleep: True if user is asleep, False if not
    :return should_answer: True if should user answer phone, False if not'''
    
    should_answer = False
    
    if is_asleep:
        should_answer = False
    elif is_morning:
        if is_mom:
            should_answer = True
        should_answer = False
    else:
        should_answer = True
    
    return should_answer
    
def four_fit_in_one(car_one, car_two, car_three, car_four, car_five):
    cars = [car_one, car_two, car_three, car_four, car_five]
    sum_of_cars = car_one + car_two + car_three + car_four + car_five
    
    #sees if one car has more capacity than the rest
    for car in (car_one, car_two, car_three, car_four, car_five):
        if car > (sum_of_cars - car):
            return True
        
    return False

def can_move(Nblocked, Sblocked, Eblocked, Wblocked, power, direction):
    if power > 15:
        if direction == "W" and not Wblocked:
            return True
        if direction == "E" and not Eblocked:
            return True    
        if direction == "S" and not Sblocked:
            return True        
        if direction == "N" and not Nblocked:
            return True        
    elif power > 1000:
        return True
    
    #if none of the above conditions are met
    return False

def get_ticket(speed, is_birthday):
    if not is_birthday:
        if speed <= 60:
            return 0
        
        if speed >= 61 and speed <= 80:
            return 2 * speed
        elif speed >= 81:
            return 3 * speed
    else:
        if speed <= 70:
            return 0
        
        if speed >= 71 and speed <= 90:
            return 2 * speed
        elif speed >= 91:
            return 3 * speed    
def hypotenuse(a, b, c):
    value = False
    
    #tests hypotenuse using pythagorean theorem
    if a**2 == (b**2 + c**2):
        value = math.sqrt(b**2 + c**2)
    elif b**2 == (a**2 + c**2):
        value = math.sqrt(a**2 + c**2)
    elif c**2 == (a**2 + b**2):
        value = math.sqrt(a**2 + b**2)
    
    #I don't think I have to check type for this despite what packet says
    return value
def investment(initial, compound_per_yr, change, yrs):
    #uses compound interest formula
    value = initial * (1 + (change/compound_per_yr)) ** (compound_per_yr * yrs)
    return value
def dessert(had_dinner, is_healthy, nut_allergy, is_cold):
    #returns what user should be told to eat
    if not had_dinner:
        return "You should eat dinner first."
    else:
        if is_healthy:
            return "You should eat a fruit salad."
        elif not is_healthy:
            if nut_allergy:
                return "You should eat a chocolate cake."
            elif not nut_allergy:
                if is_cold:
                    return "You should have peanut butter ice cream."
                else:
                    return "You should eat a peanut butter cup."