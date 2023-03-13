"""
MY BMI PROGRAM
COSC110-Introduction to programming
Fatuma ibrahim
february 9th
"""
#description:
           #An application that calculates the body mass index (BMI) of a person as well as related description of their
           #body mass index. The program will also determine how much weight to lose to move one category towards healthy

#DECLARATIONS
#constant to present the min_height
MIN_HEIGHT = 20
#constant to present the max_height
MAX_HEIGHT = 120
#constant to present the min_weight
MIN_WEIGHT = 10
#constant to present the value of BMI
BMI_CONSTANT = 703
#constant to present severely underweight
SEVERELY_UNDERWEIGHT =16
#constant to present underweight
UNDER_WEIGHT= 18.5
#constant to present healthy
HEALTHY = 25
#constant to present overweight
OVERWEIGHT= 30

#INPUT
#prompt the user to enter height in inches
height = input("please enter your height in inches: ")

#VALIDATION
#Check if height is not numeric
if not height.isnumeric():
    #if not numeric print an error message
    print("height must be numeric")
else:
    #value is numeric and is valid 
    #continue with processing
     
    #processing
    #convert the height value to a floating point
    height = float(height)
   
#check if height is between MIN_HEIGHT AND MAX_HEIGHT
if MIN_HEIGHT < height < MAX_HEIGHT :
    #if value is in range
      is_valid = True
else:
    #value not in range 
    #display an error message
    is_valid =False
    print("height must be in range")

#Prompt the user to enter weight in pounds
weight = input("please enter your weight in lbs: ")
#VALIDATION
#check if weight is not numeric
if not weight.isnumeric():
    print("weight must be numeric")
else:
    #value is numeric and is valid
    #continue with processing

    #processing 
    #convert the weight value to a floating point
    weight = float (weight )
   
#check if weight is within the range
if MIN_WEIGHT < weight:
    #if weight is in range 
    is_valid = True
else:
    #value not in range
    #display an error messge
    is_valid = False
    print("weight must be in range")

try:
    # TRY to calculate the BMI and store in a variable
    #round it to 1 decimal place
  BMI = round(weight/height**2 * BMI_CONSTANT,1)
  #check the value against the thresholds
  if BMI < SEVERELY_UNDERWEIGHT:
    #if BMI is
    category = "severely underweight"
    #target that can be reached
    target_BMI =18.5
  elif BMI < UNDER_WEIGHT:
    #if BMI is
    category = "underweight"
    #target that can be reached
    target_BMI = 25
  elif BMI < HEALTHY :
    #if BMI is 
    category = "healthy"
    #target that can be reached
    target_BMI = None
  elif BMI < OVERWEIGHT:
    #if BMI is 
    category = "overweight"
    #target that can be reached
    target_BMI=25
  else:
    #else is
    category = "obese"
    #target that can be reached
    target_BMI = 30
  #calculate the weight to lose and store it in variable 
  #round to 1 decimal place
  weight_to_lose= round( (target_BMI * height**2) / BMI_CONSTANT, 1)
  #output a formatted string containing:
  # the user input values(height,weight,bmi.category and target bmi) 
  #a message depending on BMI
  print("The BMI for a " +str(height) + "inches tall person who weighs " + str(weight)+ "pounds is "+ str(BMI)+"which is catergorized as " + str(category)+ " a healthier BMI category is" + str(HEALTHY) + " which can be raeched at" + str(target_BMI))
except ValueError: 
    #CATCH EXCEPTIONS if not numeric display an error message
    print("INPUT ERROR: \n height and weight must be numeric ")
#END
#prompt the user to enter to end the program
input("\n press enter to end the program")
    
    









