"""
My Pizza Program
COSC110-introduction to programming
Fatuma Ibrahim
5 March 2023
"""
#DESCRIPTION: An application that prompts the user to enter a diameter of a pizza in inches and presents the area of
              #each pizza slice based in multiple possible configuration the user should then be able to enter another
              #diameter or indicate they want to quit bt entering 0

#Declaration:
#constant for max_diameter, min_diameter and validation
#constant to represent max diameter
MAX_DIAMETER = 24
#constant to represent min diameter
MIN_DIAMETER = 8



#input
import math
while True:
    #while the user is required to input something
    #Validation
    try:
        #prompt the user to enter the diameter of pizza in inches 
        diameter = float(input("Enter the diameter of the pizza in inches (0 to end the program): "))
        #if user input is 0
        if diameter == 0:
            #end the program
            break
    
        #check if diameter is within the range of min_diamter to max_diameter
        if diameter < MIN_DIAMETER or diameter >MAX_DIAMETER:
            #if not in range
            #entry error : diameter must be in rage
            print("Error: Diameter must be in range")
            break
        #catch exceptions of value error
    except ValueError:
        #if not numeric 
        #error : please enter a valid numeric number
        print("error please enter a valid numeric number")

        # continue with processing
        #check the value within the thresholds
    if 8 <= diameter < 12 :
    #can be cut into 6 slices
        slices = 6
    elif 12 <= diameter < 14: 
    #slices can be 6 0r 8
        slices = 6 or 8  
    elif 14 <= diameter < 16:
    #slices can be 6 or 8 or 10
        slices= 6 or 8 or 10
    elif 16 <= diameter < 20:
    #slices can be 6 or 8 or 10 or 12
        slices = 6 or 8 or 10 or 12
    else:
    #slices can be 6 or 8 or 10 or 12 or 16
        slices = 6 or 8 or 10 or 12 or 16
    #calculate for radius
    radius = diameter/2
    #calculate area per slice 
    #round it up to 2 decimal places
    area_per_slice = round ( math.pi * radius ** 2 / slices, 2)
     
    
    #output
    #print diameter inputed
    print(f"Pizza Diameter: {diameter}")
    #print slices required
    print(f" cut in {slices} slices results in an area of {area_per_slice} per slice")