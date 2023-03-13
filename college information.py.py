"""
mycollege program information
COSC1100-Planning for validation
Fatuma Ibrahim
feb 2023


Description:
     An application that prompts for and then accepts input of user's name, the college program they enrolled in,
     and the number of years it takes to complete the program 
"""
             
#Declarations
#constant interger for the minimum number of years a program can be 
MIN_YEARS = 1
#constant interger for the maximum number of years can be 
MAX_YEARS = 3

#if user input is valid or not, defaulted to false
is_valid = False

#input
#prompt the user to enter their name and store in Variable student_name
student_name = input('please enter your name: ')

#validation
#check if user input for student name is empty
if student_name != "":
    #if not empty
    is_valid = True
else:
    #else empty string 
    #display error message
    is_valid = False
    print("student name cannot be empty")
#check if valid 
if is_valid:
    #input is valid 
    #continue with validation
    #prompt the user to enter their college program name , and store in a variable college_program
    college_program = input("please enter the college program: ")

    #check if user input for college program is empty
    if college_program != "":
        #if not empty
        is_valid = True
    else:
        #empty string
        #display error message 
        is_valid = False
        print("college program cannot be empty")
    
    #check if valid
    if is_valid:
        #input is valid 
        #continue with validation
        #prompt the user to enter the number of year to complete the program, and store in a variable years of program
        years_of_program = input("please enter the number of years for the program: ")
        #check if years of program is numeris
        if years_of_program.isnumeric():
            years_of_program = int(years_of_program)
            is_valid = True
        else:
            #not numeric
            #display error message
            is_valid = False
            print("number of years must be numeris")
        #check if the years entered  is between MIN_YEARS AND MAX_YEARS
        if MIN_YEARS <= years_of_program <= MAX_YEARS:
            #if years is in range 
            is_valid = True
            print("name: " + student_name)
            print("program: " + college_program)
            print("years to complete:" +str( years_of_program))
        else:
            #years of program not in range
            #display error message
            is_valid = False
            print("number of years must be in the range of MIN_YEARS and MAX_YEARS")




    
         
          


