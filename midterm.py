"""
MY MIDTERM PROGRAM
COSC1100-INTRO TO PROGRAMMING
FATUMA IBRAHIM
9 MARCH
"""
#DESCRIPTION:A program that calculates your midterm mark and asks the user for their marks for each assessment #
             # ordered by the type. the assessment include pre-class activity, in-class activity , Assignments hence calculates#
             #  and displays the users grade as a percentage for each assessment.
#DECLARATION
#Declare constants to represent the maximum number of points for the each assingment type CEs (4), PCA (4), Labs (1)
PRE_CLASS_EXERCISE_COUNT = 4
CLASS_ASSINGMENT_COUNT = 4
LAB_ASSIGNMENT_COUNT = 1
#Declare constants to represent each of the category maximum values CE (0.16), PCA (0.16), Lab (0.10).
PRE_CLASS_EXERCISE_WORTH = 0.16
CLASS_ASSINGMENT_WORTH = 0.16
LAB_ASSIGNMENT_WORTH = 0.10
# Declare global variable lists for each of the evaluation types
pre_class_exercise_grade = list()
class_activities_grades = list()
lab_assignment_grades = list()

# Delcare gobal varaibles for the average grades of each evaluation type
average_pre_class_exercise = 0.0
average_class_activities = 0.0
average_lab_assignment = 0.0
# Delcare constants for minimum and maxium grade (0 to 100 inclusive)
min_grade = 0
max_grade = 100 
# Declare a global variable for the total grade overall
total_grade = 0.0

from statistics import mean
#for each Class Exercise index in the range of PRE_CLASS_EXERCISE_COUNT (4)
for index in range(0 , PRE_CLASS_EXERCISE_COUNT):
    need_input = True

    while need_input :
        try:
            # prompt the user for their grade on each of the PCE as a real number out of 100
            user_input = float(input("\n please enter the grade you received out of 100 for pre_class exercise " + str(index + 1) + ":"))
        # Check to see if the value is in the valid grade range
            if min_grade <= user_input <= max_grade :
                pre_class_exercise_grade.append(user_input)
                # Mark the current loop as sucessful
                need_input = False
            else:
                # If it is an invalid grade
                # Display error message to user
                print("The grade must be a value between "  + str(min_grade) and + str(max_grade) + " inclusive . please try again later." )
        except:
        # Display the error to the user that the grade entered must be numerical
            print("the grade must be a numerical number" )
      # Determine the average PCEs
for index in range(0 , CLASS_ASSINGMENT_COUNT):
    need_input = True

    while need_input :
        try:
            # prompt the user for their grade on each of the CE as a real number out of 100
            user_input = float(input("\n please enter the grade you received out of 100 for class exercise " + str(index + 1) + ":"))
        # Check to see if the value is in the valid grade range
            if min_grade <= user_input <= max_grade :
                class_activities_grades.append(user_input)
                # Mark the current loop as sucessful
                need_input = False
            else:
                # If it is an invalid grade
                # Display error message to user
                print("The grade must be a value between "  + str(min_grade) and + str(max_grade) + " inclusive . please try again later." )
        except:
        # Display the error to the user that the grade entered must be numerical
            print("the grade must be a numerical number" )
for index in range(0 , LAB_ASSIGNMENT_COUNT):
    need_input = True

    while need_input :
        try:
            # prompt the user for their grade on each of the PCE as a real number out of 100
            user_input = float(input("\n please enter the grade you received out of 100 for lab assignment " + str(index + 1) + ":"))
        # Check to see if the value is in the valid grade range
            if min_grade <= user_input <= max_grade :
               lab_assignment_grades.append(user_input)
                # Mark the current loop as sucessful
               need_input = False
            else:
                # If it is an invalid grade
                # Display error message to user
                print("The grade must be a value between "  + str(min_grade) and + str(max_grade) + " inclusive . please try again later." )
        except:
        # Display the error to the user that the grade entered must be numerical
            print("the grade must be a numerical number" )  

      # Determine the average PCEs      
average_pre_class_exercise = mean(pre_class_exercise_grade)
# Determine the total grade overall
total_grade += average_pre_class_exercise * PRE_CLASS_EXERCISE_WORTH 

average_class_activities = mean(class_activities_grades)
# Determine the total grade overall
total_grade += average_class_activities * PRE_CLASS_EXERCISE_WORTH
average_lab_assignment = mean(lab_assignment_grades)
# Determine the total grade overall
total_grade += average_lab_assignment * PRE_CLASS_EXERCISE_WORTH 
#OUTPUT
#output the average PCEs 
print(f" average_pre_class_exercise:{average_pre_class_exercise}")

#output the average CEs 
print(f" average_class_exercise:{average_class_activities}")

#output the average lab assignment
print(f"Average_lab_assignment: {average_lab_assignment}")
#output the total grade
total_grade = round(total_grade / (CLASS_ASSINGMENT_WORTH + PRE_CLASS_EXERCISE_WORTH + LAB_ASSIGNMENT_WORTH),2)
print(f"Total midterm Grade: {total_grade}")
# Prompt the user to press enter to exit
input("\nPress Enter to exit program.")

