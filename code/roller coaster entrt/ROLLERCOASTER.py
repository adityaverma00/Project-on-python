height_input=input("wirte your height")
if height_input>="120":  #If height is greater than or equal to 120
    print("you are eligible congrats. please choose your plan")
    age_input=input("write your age for price")
    if age_input<="12": #If age is less than or equal to 12
        print("ticket price is $5")
    elif age_input<="17" and age_input>"12": #If age is less than and equal to 17 and greater than 12
        print("ticket price is $7")
    elif age_input>"18": #If age is greater than 18
        print("ticket price is $12")
    else:
        print("")
    photo_user=bool(input("do u want to take pictures")) #question
    if photo_user==True: 
        print("charge is $3") #If yes 
    else:
        print("have fun") #If no
else:
    print("you are little too short.sorry")
