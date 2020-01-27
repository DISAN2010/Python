#Main starts from here
Start_Distance_Travelled=input("Enter the starting distance : ")
Start_Distance_Travelled=int(Start_Distance_Travelled)
Current_Distance_Travelled=input("Enter the distance travelled till now : ")
Current_Distance_Travelled=int(Current_Distance_Travelled)
Distance_Travelled=Current_Distance_Travelled-Start_Distance_Travelled
print("Distance travelled till now : ", Distance_Travelled)
Fuel_Consumption=input("Enter how much fuel filled : ")
Fuel_Consumption=float(Fuel_Consumption)
Mileage=Distance_Travelled/Fuel_Consumption
print("Your Mileage is : ", Mileage)
