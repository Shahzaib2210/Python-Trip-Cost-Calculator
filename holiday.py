'''
# Pseudo code
1 - Give city options and take city input from user want to travel and store it in city_flight variable.
2 - Take number of nights input from user want to stay at hotel and store in num_nights variable.
3 - Take number of days input from user want to hire a car and store in hire_days variable.
4 - Now create function hotel_cost with taking input parameter num_of_nights and return return (str(num_of_nights * 50)) after calculation.
5 - Now create function plane_cost with input parameter city_name, apply check on city_name and return flight cost according to city name and if user enter invalid city name return 0.
6 - Now create function car_rental with taking input parameter num_of_days and return return (str(num_of_days * 30)) after calculation. 
7 - Now create function holiday_cost with input parameter hotel, plane, car
    1 - Calculate the total_cost by adding hotel + plane + car and store in total_holiday_cost variable.
    2 - If plane value is 0, return total cost and a message "Invalid city selected, please select a valid city from options. Flight cost is not included in it."
    3 - else return total_holiday_cost.
8 - Now call the function hotel_cost and print (f"The hotel cost is: £{hotel_cost(num_of_nights = num_nights)}.")
9 - Now call the function plane_cost and print (f"The flight cost is: £{plane_cost(city_name = city_flight)}.")
10 - Now call the function car_rental and print (f"The car rent cost is: £{car_rental(num_of_days = hire_days)}.")

11 - Now call the function holiday_cost and print (f"The total holiday cost is : £{holiday_cost(hotel=hotel_cost(num_of_nights = num_nights),
                                                   plane=plane_cost(city_name = city_flight),
                                                   car=car_rental(num_of_days = hire_days))}.")
'''
city_flight = input("""London
Edinburgh
Manchester 
Aberdeen
Please select the city you want to travel: """) # Taking city name input.

num_nights = int(input("Please enter the number of nights you want to stay at hotel: ")) # Taking number of night user want to stay at hotel input.
hire_days = int(input("Please enter the number of days you want to hire a car: ")) # Taking number of days user want to hire a car input.

def hotel_cost(num_of_nights): # Function calculating hotel_cost according to number of night user want to stay inputs.
    return (str(num_of_nights * 50))

def plane_cost(city_name): # Function returning plane_cost according to city_name input.
    if city_name == "London":
        return (str("60"))
    elif city_name == "Edinburgh":
        return (str("60"))
    elif city_name == "Manchester":
        return (str("40"))
    elif city_name == "Aberdeen":
        return (str("45"))
    else:
        return str(0)
    
def car_rental(num_of_days): # Function returning car rent cost according to number of days user want to hire a car input.
    return (str(num_of_days * 30))

def holiday_cost(hotel, plane, car): # Function returning total holiday cost by adding hotel, plane and car cost
    total_holiday_cost = int(hotel) + int(plane) + int(car)
    if plane == "0":
        return f"""{total_holiday_cost}
Invalid city selected, please select a valid city from options. Flight cost is not included in it."""
    else:
        return str(total_holiday_cost)

print("======================= Hotel Cost ==================================")
print()
print (f"The hotel cost is: £{hotel_cost(num_of_nights = num_nights)}.") # printing hotel cost.
print()
print("======================= Plane Cost ===================================")
print()
print (f"The flight cost is: £{plane_cost(city_name = city_flight)}.") # printing plane cost.
print()
print("====================== Car Rent Cost ==================================")
print()
print (f"The car rent cost is: £{car_rental(num_of_days = hire_days)}.")# printing car rent cost.
print()
print("===================== Total Holiday Cost ==============================")
print()
print (f"The total holiday cost is : £{holiday_cost(hotel=hotel_cost(num_of_nights = num_nights),
                                                    plane=plane_cost(city_name = city_flight),
                                                    car=car_rental(num_of_days = hire_days))}.") # printing total holiday cost.
print()
print("=======================================================================")