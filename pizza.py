"""
My Pizza Program
COSC110-introduction to programming
Fatuma Ibrahim
5 March 2023
"""
#DESCRIPTION: An application that prompts the user to enter a diameter of a pizza in inches and presents the area of
              #each pizza slice based in multiple possible configuration the user should then be able to enter another
              #diameter or indicate they want to quit bt entering 0

#Description:
#constant for max_diameter, min_diameter and validation
#constant to represent max diameter
MAX_DIAMETER = 24
#constant to represent min diameter
MIN_DIAMETER = 8
#input
import math
while True :
#while the user is required to input something
  #prompt the user to enter the diameter of pizza in inches   
  diameter = float(input("enter the diameter of pizza in inches(0 to end the program): "))
  #if user input is 0
  if diameter ==0:
    #end the program    
        break
  #Validation
  try:
     #check if diameter is within the range of min_diamter to max_diameter
    if 8<= diameter <= 24:
        
        # continue with processing
        #check the value within the thresholds
        if diameter < 12:
          #can be cut into 6 slices
            num_slices = 6
        elif diameter < 14:
           #slices can be 6 0r 8 
            num_slices =  8
            
        if diameter < 16:
           #slices can be 6 or 8 or 10  
            num_slices = 10
        if diameter <20:
           #slices can be 6 or 8 or 10 or 12
            num_slices = 12
        else:
         #slices can be 6 or 8 or 10 or 12 or 16
            num_slices = 16
        #calculate the radius
        radius = diameter /2
        #calculate the area of each slice
        area_per_slice=round( math.pi * radius**2/num_slices , 2)

        #output
        #print pizza diameter
        print(f" pizza diameter : {diameter}")  
        #print the number of slices and the area
        print(f"cut in {num_slices} slices results in an area of {area_per_slice} per slice.\n")
    else:
        #error:
        #diameter musr be in range
        print("error: the diameter must be in range.\n ")
        #catch exception
  except ValueError :
      #invalid input
      #diameter must be within the range
      print ("error: The diameter must be numeric.\n")