width = int(input("Type the width in metres: "))
length = int(input("Type the length in metres: "))
height = int(input("Type the height in metres: "))

volume_cuboid = (width * height * length)
surface_area = 2 * ((width * length) + (height * width) + (length * height))

print("\nSurface area: {} m2" .format(surface_area))
print("Volume area: {} m3 " .format(volume_cuboid))