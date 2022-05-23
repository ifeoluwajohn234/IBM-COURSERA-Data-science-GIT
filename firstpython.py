#display the output
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	print(km)
convert_distance(55)
my_trip_miles = 55


# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
