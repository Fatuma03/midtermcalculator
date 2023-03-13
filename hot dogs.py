"""
My hot dog program
cosc 110 - introduction to programming
Fatuma ibrahim
feb 16
"""
#description:
            #an application that determines which type of hot dog
            #is more popular and displays the number sold for each type type of hotdog
            #with a percentage of the total number of hot dogs 
#declarations
#constant to represent the Hotdogs
#constant interger for traditional hot dog
Traditional = 1
#constant interger for veggie dog
veggie_dog = 2
#constant interger for curry hot dog
curry_hot_dog = 3
#comment
tally_end = 4
#global boolean variable to store a flag for user input
need_input = True
#comment
total_sold = 0
#comment
traditional_sold  = 0
#comment
veggie_sold = 0
#comment
curry_sold = 0
#global variable to store user input
user_input = ""
END_PROGRAM = "END"
message = ""
#INPUT
while need_input :
    #while the user is required to input something
    
    #validation
   try:
        #Prompt the user to enter menu option and try to parse it as an interger
         menu_option = int(input("\n\n1. Add Traditional Hot dog \n2. Add veggie Hot dog \n3. Add curry hot dog \n4. Tally All and End \n please select a menu option: "))
         if Traditional <= menu_option <= tally_end:
            #continue with incrementing
            if  menu_option == Traditional:
            #if the user enters 1 increment by 1
             traditional_sold +=1
            elif menu_option == veggie_dog:
            #if the users enters 2 increment by 1
             veggie_sold +=1
            elif menu_option == curry_hot_dog:  
            #if the user enters 3 increment by 1   
             curry_sold +=1 
           
            else:
             menu_option == tally_end 
               #if the user enters 4 tally up all entry
             total_sold = traditional_sold + veggie_sold + curry_sold
             print(total_sold)
                  #calculate percentages
                  #the percenatge for tradition
             if total_sold > 0:
               percentage_tradition = (traditional_sold/total_sold)*100
                  #the percentage for veggie
               percentage_veggie = (veggie_sold/total_sold)*100
                  #the percentage for curry
               percentage_curry = (curry_sold/ total_sold)* 100
             else:
               #division is zero
               #display error message
               print("zero division error")
            
         else:
            #display an entry error message
            print("\nEntry Error . \n\n menu option was invalid. it must be within range")
         #output percentages of hot dogs
         print(percentage_tradition)
         print(percentage_veggie)
         print(percentage_curry)
         
   except : 
      #Check to see if user input is equal to ending key
      if user_input == END_PROGRAM:
      #update the need input to false
        need_input = False
        #prompt the  user to press enter to end the program
        input("\n press enter to end the program")
      else:
      #catch exceptions
         #if not a whole number or numeric display error
         print("\nEntry Error.\nMenu option was invalid. it must be a whole number")
      
        


