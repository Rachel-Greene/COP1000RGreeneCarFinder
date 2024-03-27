## This is the program to run the AutoCountry Vehicle Finder app, version 0.1
# Functions 
def checkValidInput(testInput):
  if testInput == "1":
    return True
  elif testInput == "2":
    print("Thank you for using AutoCountry Car Finder, good-bye!")
    exit()
  else:
    print(f"Sorry, {testInput} is not a valid input.\nPlease try again with the correct input from the provided list.")
    exit()


## ----- Vehicles Array ----- ##
carMakes = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]

## ----- Customer Messages ----- ##
welcomeMessage = """
  ********************************
  AutoCountry Vehicle Finder v0.1
  ********************************
  Please enter the following number from the following menu:
   \n
    1. PRINT all Authorized Vehicles
    2. Exit
"""
choice1Message = "The AutoCountry sales manages has authorized the purcha and selling of the following vehicles:"

## Customer input, Validation ##
print(welcomeMessage)
customerInput = input()
trueInput = checkValidInput(customerInput)

## Logic, Customer Output ##
if trueInput == True:
  print(choice1Message)
  print(carMakes)
  


