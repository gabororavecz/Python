packet= int(40)
student = int(14)

sweets_per_child = int(packet / student)
sweets_remain = int(packet % student)

print("Number of sweets per children: "+ str(sweets_per_child ))
print("Number of sweets that the teacher keeps: " + str(sweets_remain))