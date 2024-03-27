## This is the program to run the AutoCountry Vehicle Finder app, version 0.1 ##
## ------------------------------ Functions ------------------------------ ##
def checkValidInput(testInput):
  if testInput == "1":
    return True
  elif testInput == "2":
    print("\nThank you for using AutoCountry Car Finder, good-bye!")
    exit()
  else:
    print(f"Sorry, {testInput} is not a valid input.\nPlease try again with the correct input from the provided list.")
    exit()


## --------------------------- Declerations ---------------------------- ##
carMakes = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
welcomeMessage = """
  ********************************
  AutoCountry Vehicle Finder v0.1
  ********************************
  Please enter the following number from the following menu:
   \n
    1. PRINT all Authorized Vehicles
    2. Exit
"""
choice1Message = "\nThe AutoCountry sales manages has authorized the purchase and selling of the following vehicles: "


## --------------------- Customer input, Validation --------------------- ##
print(welcomeMessage)
customerInput = input()
trueInput = checkValidInput(customerInput)


## ----------------------- Logic, Customer Output ----------------------- ##
if trueInput == True:
  print(f"{choice1Message}")
  for a in range(0,5):
    print(carMakes[a])
