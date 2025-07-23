from math import sqrt
import os


# Exercice 2
print("Exercice 2")
## question 1
print("question-1")
os.system("python --version")


## question 2
print("question-2")
print(10 + 3)  # addition
print(10 - 3)  # soustraction
print(10 / 3)  # division
print(10 * 3)  # multiplication
print(10 % 3)  # modulo
print(10 ^ 3)  # exposant
print(10 // 3)  # division entière

## question - 3
print("question-3")
print("Victor" + " Espoir" + "Togo" + "je profite de 30 jours de python")

## question - 4
print(type(10 // 9))
print(type(8 // 3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finlande"]))
print(type("Victor" + " Espoir" + "Togo" + "je profite de 30 jours de python"))

# Exercice 3
print("Exercice 3")
## question 1
print("String data")
print(1 == 1, 2 == 3)
print([1, "list", 2, "amorphe"])
print((10, 8))
print({1, 2, 3, 7, 10})
print({"username": "runner", "password": ".......", "age": 20, "is_married": False})
print(" question-1")
## question 2
print(" question-2")
point1 = (2, 3)
point2 = (10, 8)
distance_euclidienne = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print(" distance euclidienne: ", distance_euclidienne)
