pi = 3.14159

outer_radius = float(input("Enter the radius of the outer surface: "))
inner_radius = float(input("Enter the radius of the inner surface: "))
height = float(input("Enter the height of the hollow cylinder: "))

outer_radius_squared = outer_radius ** 2
inner_radius_squared = inner_radius ** 2

volume = pi * height * (outer_radius_squared - inner_radius_squared)

print(f"The volume of the hollow cylinder is: {volume:.4f}")