import time

#Define BMI function
def bodymassindex(weight, height):
    return round(weight / (height/100) ** 2, 2)

print("Welcome to the Body Mass Index (BMI) calculator!")
time.sleep(1)
print("Let's calculate your BMI")
time.sleep(1)

#User input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

#Display BMI 
BMI = bodymassindex(weight, height)
print ("Your BMI is:", BMI)

if (BMI < 18.5):
    print("You are underweight")
elif (BMI <= 24.9):
    print("Your weight is within the normal range")
elif (BMI < 30):
    print("You are overweight")
else:
    print("You are obese")   



