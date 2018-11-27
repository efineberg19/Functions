#!/ysr/bin/python
#functions_tester.py

'''Allows user to pick and try out functions defined in functions.py'''

__author__ = "Beth Fineberg"
__version__ = "1.0"

import functions
import utility
import turtle

def main():
    
    done = False
    
    while not done:
        
        print("SELECT FROM THE FOLLOWING MENU ITEMS:\n"
              "1: Draw a polygon\n"
              "2: Draw random polygons!\n"
              "3: Draw some stairs\n"
              "4: Should you answer your phone?\n"
              "5: Vehicle check\n"
              "6: Can your player move?\n"
              "7: Will you get a speeding ticket?\n"
              "8: Hypotenuse finder\n"
              "9: Investment worth\n"
              "10: Pick dessert\n"
              "0: QUIT!\n")

        selection = int(input("YOUR SELECTION: "))
        
        if selection == 1:
            #Draw a Polygon selected
            num_sides = int(input("How many sides would you like your shape to "
                                  + "have? "))
            side_length = int(input("How long would you like the sides to be? "))
            
            t = turtle.Turtle()
            w = turtle.Screen()
            
            #draws polygon according to user's specification
            functions.draw_polygon(num_sides, side_length, t, w) 
            
            input("\nPress enter to continue.")
        
        elif selection == 2:
            #Draw random polygons selected
            num_poly = int(input("How many polygons would you like drawn? "))
            
            t = turtle.Turtle()
            w = turtle.Screen()
            
            functions.random_polygons(num_poly, t, w)
            
            input("\nPress enter to continue.")
 
        elif selection == 3:
            #Draw some stairs selected
            num_stair = int(input("How many stairs would you like drawn? "))
            
            t = turtle.Turtle()
            w = turtle.Screen()            
            
            functions.draw_stairs(num_stair, t, w) 
            
            input("\nPress enter to continue.")
            
        elif selection == 4:
            #Should you answer you phone? selected
            print("I will ask you three questions to determine if you should " +
                  "pick up the phone. Please respond Y/N or yes/no.")
            
            morning = utility.yes_answer(input("Is it morning? "))
            mother = utility.yes_answer(input("Is it your mother calling? "))
            asleep = morning = utility.yes_answer(input("Are you asleep? "))
            
            ans = functions.should_answer_cell(morning, mother, asleep) 
            
            if ans:
                print("You should definitely pick up the phone!")
            else:
                print("You should not pick up the phone.")
                
            input("\nPress enter to continue.")
        
        elif selection == 5:
            #Vehicle check selected
            car_one_cap = int(input("How many people can fit into the first "
                                    + "car? "))
            car_two_cap = int(input("How many people can fit into the second "
                                    + "car? "))   
            car_three_cap = int(input("How many people can fit into the third "
                                    + "car? "))        
            car_four_cap = int(input("How many people can fit into the fourth "
                                    + "car? "))   
            car_five_cap = int(input("How many people can fit into the fifth "
                                    + "car? "))              
                                    
            ans = functions.four_fit_in_one(car_one_cap, car_two_cap, 
                                            car_three_cap, car_four_cap, 
                                            car_five_cap)   
            if ans:
                print("One of the cars can fit all the students that could fit "
                      + "in the 4 remaining cars.")
            else:
                print("None of the cars can fit all the students that could fit "
                      + "in the 4 remaining cars.")
                
            input("\nPress enter to continue.")
            
        elif selection == 6:
            #Can player move? Selected
            print("I will ask you several questions to determine if your " +
                  "character should be able to move. Please respond with Y/N "
                  + "or yes/no if it asks a yes or no question.")
            
            north_block = utility.yes_answer(input("Is North blocked? "))
            south_block = utility.yes_answer(input("Is South blocked? "))
            east_block = utility.yes_answer(input("Is East blocked? "))
            west_block = utility.yes_answer(input("Is West blocked? "))
            
            power_level = int(input("What is your character's power? "))
            
            direction = input("What direction is your character moving in (N/"
                              + "S/E/W)? ")
            
            ans = functions.can_move(north_block, south_block, east_block,
                                     west_block, power_level, direction)
            
            if ans:
                print("Your character moves ", direction, "!", sep='')
            else:
                print("Your character is unable to move.")
                
            input("\nPress enter to continue.")
                
        elif selection == 7:
            #Will you get a speeding ticket? selected
            sp = int(input("What is your speed? "))
            birthday = input("Is it your birthday? ")
            
            ans = functions.get_ticket(sp, birthday)
            
            print("Your ticket will be for $", ans)
            
            input("\nPress enter to continue.")
        elif selection == 8:
            #Hypotenuse finder selected
            a = int(input("Give me the length for a side of a triangle: "))
            b = int(input("Give me another length for a side of a triangle: "))
            c = int(input("Give me one more length for a side of a triangle: "))
            
            ans = functions.hypotenuse(a, b, c)
            
            if type(ans).__name__ == "bool":
                print("There is no hypotenuse")
            elif type(ans).__name__ == "float":
                print("The length of the hypotenuse is:", ans)
                
            input("\nPress enter to continue.")
        elif selection == 9:
            #Investment worth selected
            initial_investment = int(input("How much would you like to invest? "))
            compounds_per_year = int(input("How many times per year does your " 
                                           + "investment compound? "))
            percent_change = float(input("At what percentage (in decimall form)"
                                         + " will your investment"
                                         + " change after each \ncompound? "))
            years = int(input("After how many years after the initial investment"
                              + " would you like \nto calculate the value for? "))
            
            print("Your investment will be worth $" + 
                  str(functions.investment(initial_investment, compounds_per_year, 
                  percent_change, years)) + " after " + str(years) + " years.")
            input("\nPress enter to continue.")
        elif selection == 10:
            #Pick dessert selected
            print("I will ask you questions to determine what you should eat",
                  "for dessert.")
            ate_dinner = utility.yes_answer(input("Have you eaten dinner? "))
            healthy = utility.yes_answer(input("Do you like healthy desserts? "))
            nut = utility.yes_answer(input("Do you have a nut allergy? "))
            cold = utility.yes_answer(input("Do you like cold desserts? "))
            
            print(functions.dessert(ate_dinner, healthy, nut, cold))
            
            input("\nPress enter to continue.")
        else:
            done = True
        
main()