#Input
height_feet = float(input("\nFeet: "))
height_inches = float(input("Inches: "))

#Calculation
conversion_feet = float(height_inches / 12)
total_height = float((height_feet + conversion_feet))

#Convertion:
height_kilometres = float(total_height / 3281)
height_metres = float(total_height / 3.281)
height_centimetres = float(total_height * 30.48)
height_milimetres = float(total_height * 305)

#Output
print("\nHeight in kilometres: {}" .format(height_kilometres))
print("Height in metres: {}" .format(height_metres))
print("Height in centimetres: {}" .format(height_centimetres))
print("Height in milimetres: {}" .format(height_milimetres))