#can covers=5.1m² d=15cm h=30cm
#floor (40cm+30cm)*2=140cm * 340cm = 47600cm = 476m²/5.1m² = 93.3 cans so 94
#d/2=r 3.14*r2*h = 3.14*7.5*7.5*0.3 =
#Area of floor and ceiling= " + str(area_1))
import math
#Variables
#-Cans
short_can= float(30)
long_can= float(40)
height_can= float(3.4)
can_paint_covers= float(5.1)
#-Box
length_box= float(0.6)
width_box= float(0.3)
height_box = float(0.35)

can_diameter = float(0.15)
can_r= float(can_diameter/2)
can_height = float(0.3)
pi = float(3.14)
#Calculations

can_volume = float(pi * (can_r * can_r) * can_height) #Can Volume
box_volume = float(length_box * width_box * height_box) #Box Volume


area_1 = float ((short_can + long_can) * height_can * 2) #Area of floor and ceilings
cans_required = math.ceil(area_1 / can_paint_covers) #Number of cans
number_of_full_boxes = math.floor(box_volume/can_volume) #Number of full boxes
number_of_cans_in_box = math.floor(cans_required / number_of_full_boxes) #Numbet of cans in box
cans_not_packed = math.floor(cans_required-(number_of_cans_in_box*number_of_full_boxes))

#Output
print("Number of Cans required: " + str(cans_required))
print("Number of cans in box: " + str(number_of_cans_in_box))
print("Number of full boxes: " + str(number_of_full_boxes))
print("Cans not packed in boxes: " + str(cans_not_packed))
