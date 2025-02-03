#promp for the name
name = input("Input your name: ")
#Promp for date of birth 
DOB = input("Input year of birth: ")
DOB = int(DOB)
#Calculate the age as per 2024
age = 2024 - DOB
if age >=18:
    print(f"\nName: {name.title()} \nAge: {age} \nEvaluation: Congratulations, you are elligible to vote. ")
else:
    print(f"\nName: {name.title()} \nAge: {age} \nEvaluation: Sorry, you are not elligible to vote as per now, try  next time.")
