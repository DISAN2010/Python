#Mileage
Start_Distance_Travelled=input("Enter the starting distance from odometer : ")
Start_Distance_Travelled=int(Start_Distance_Travelled)
Current_Distance_Travelled=input("Enter the distance travelled till now : ")
Current_Distance_Travelled=int(Current_Distance_Travelled)
Distance_Travelled=Current_Distance_Travelled-Start_Distance_Travelled
print("Distance travelled till now : ", Distance_Travelled)
Fuel_Consumption=input("Enter how much fuel filled : ")
Fuel_Consumption=float(Fuel_Consumption)
Mileage=Distance_Travelled/Fuel_Consumption
print("Your Mileage is : ", Mileage)

Bang_To_Goa = 560
count = 0
print("Travel started from Bangalore")

while(Distance_Travelled < Bang_To_Goa):
    print("Stopped for fuel")
    count = count + 1
    Bang_To_Goa = Bang_To_Goa - Distance_Travelled
    print("Kilometers to reach Goa", Bang_To_Goa)
else:
    print("Reached Goa !!!")

print("Number of stops for fuel : ", count)
