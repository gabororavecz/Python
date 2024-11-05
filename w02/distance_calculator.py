#Input
u = float(input("Initial velocity (m/s): "))
a = float(input("Acceleration (m/s²): "))
t = float(input("Time taken (s): "))


#Calculation
s = (u * t)
h = pow(t, 2)
c = (0.5 * a * h)
result = (u + c)
#Output
print("\nDistance calculator: {}m" .format(result))