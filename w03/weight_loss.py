cycle_cals_per_hour = 200
running_cals_per_hour=475
swimming_cals_per_hour=275

cycle_hours=float(input("Please enter hours spent cycling: "))
running_hours=float(input("Please enter hours spent running: "))
swimming_hours=float(input("Please enter hours spent swimming: "))

total_cycle_cals=cycle_hours*cycle_cals_per_hour
total_running_cals=running_hours * running_cals_per_hour
total_swimming_cals=swimming_hours*swimming_cals_per_hour

total_cals_burnt=total_cycle_cals + total_running_cals + total_swimming_cals

total_pounds_lost = total_cals_burnt / 3500

print("You have burnt {:.2f} calories and lost {:.2f} pounds".format(total_cals_burnt, total_pounds_lost))