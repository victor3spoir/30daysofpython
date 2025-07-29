### day-03
# 1
import math

age = 20
height = 1.71
complex = 4 + 2j

# 4
triangle_base = float(input("Enter base: "))
triangle_height = float(input("Enter height: "))
print("The area of the triangle is ", (0.5 * triangle_base * triangle_height))

# 5
triangle_a = float(input("Enter side a: "))
triangle_b = float(input("Enter side B: "))
triangle_c = float(input("Enter side C: "))
print("The perimeter of the triangle is ", triangle_a + triangle_b + triangle_c)

# 6
rectangle_length = float(input("Enter rectangle length : "))
rectangle_width = float(input("Enter rectangle width : "))
rectangle_area = rectangle_length * rectangle_width
rectangle_permiter = rectangle_length + rectangle_width
print("The rectangle perimeter is ", rectangle_permiter)
print("The rectangle area is ", rectangle_area)

# 7
circle_radius = float(input("Enter circle radius : "))
circle_circum = circle_radius * 2 * (22 / 7)
circle_area = circle_radius**2 * (22 / 7)
print("The circle circum is ", circle_circum)
print("The circle area is ", circle_area)

# 8
slope_x_intercept = 2 * 0 - 2
slope_y_intercept = 2 / 2

# 9
p_1 = (2, 2)
p_2 = (6, 10)
m = (p_2[1] - p_1[1]) / (p_2[0] - p_1[0])
euclidant_distance = math.sqrt((p_2[0] - p_1[0]) ** 2 + (p_2[1] - p_1[1]) ** 2)

# 10
print(2.0 == 2)

# 11
y = lambda x: x**2 + x * 6 + 9
print("y is equal to 0 when x=3", y(-3))
print("result is", -(3**2) + -3 * 6 + 9)


# 12
python_length = len("python")
dragon_length = len("dragon")
print(python_length > dragon_length)

# 13
print("on" in "python")
print("on" in "dragon")

# 14
print("jargon" in "I hope this course is not full of jargon")

# 15
print("on" not in ("python" and "dragon"))

# 16
print(float(len("python")))
print(str(len("python")))

# 17
even_number = 4
print("The number is even if number%2==0", even_number % 2 == 0)

# 18
result_18 = (7 // 3) == int(2.1)
print(result_18)

# 19
result_19 = type("10") == type(10)
print(result_19)

# 20
result_20 = int(9.8) == 10
print(result_20)

# 21
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
print("Your weekly earning is ", hours * rate_per_hour)

# 22
number_of_year = int(input("Enter number of years you have lived: "))
total_seconds = number_of_year * 365 * 24 * 3600
print(
    "You have lived for ",
    total_seconds,
    " seconds",
)

# 23
for nbre in range(1, 6):
    print(
        nbre,
        1,
        nbre**2,
        nbre**3,
    )
