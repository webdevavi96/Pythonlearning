# print "Normal", "Low Fever", "High Fever" using if-elif-else

temp = 37.5

if temp > 37.5:
    print("High Fever")

elif temp < 37.5:
    print("Low Fever")

else:
    print("Normal")
    
    
# Recomend puppy food if dog age is < 2 other wise recomend senior food, if cat age is < 2, recomend junior cat food otherwise senior food.

pet = str(input("What is your pet, Cat or Dog?: "))
pet_age = int(input("Enter the age of your pet: "))


try:
    if pet == "Dog" or pet == "dog":
        pet_food = "Dog Food" if pet_age >=2 else "Puppy Food"
        
    elif pet == "Cat" or pet == "cat":
        pet_food = "Junior Cat Food" if pet_age >=2 else "junior Cat Food"
        
    else:
        print("Please Enter All Details!")
        
    print("Your pet is a:",pet, "and food recomendation for your pet is:", pet_food)
    
except Exception:
    print("An Error occured, Please enter a valid Input!")
    
except ValueError:
    print("Enter a valid Value!")