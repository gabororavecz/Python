#Input
seconds = int(input("Type seconds: "))

#Calculation
hours = int((seconds / 3600))
minutes = int((((seconds % 3600) / 3600) * 60))
seconds_result = (seconds - ((hours * 3600) + (minutes * 60)))
#Output
print("\n{:<15}{:<15}{:<15}{:<15}" .format("Input", "Hours", "Minutes", "Seconds"))
print("{:<15.0f}{:<15.0f}{:<15.0f}{:<15.0f}" .format(seconds, hours, minutes, seconds_result))