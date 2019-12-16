# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
side_a = int(input("Enter the length of side 'a' of a triangle:"))
side_b = int(input("Enter the length of side 'b' of a triangle:"))
side_c = int(input("Enter the length of side 'c' of a triangle:"))

if side_a == side_b == side_c:
    print(
        f"A triangle with sides {side_a}, {side_b} and {side_c} is an equilateral triangle"
    )

elif side_a != side_b and side_a != side_c:
    print(
        f"A triangle with sides {side_a}, {side_b} and {side_c} is a scalene triangle"
    )

else:
    print(
        f"A triangle with sides {side_a}, {side_b} and {side_c} is an isoceles triangle "
    )
