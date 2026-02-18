print("Tests for equality and inequality with strings")
name_1 = 'Roger Federer'
name_2 = 'roger federer'

print("name_1 == name_2 I predict False")
print(name_1 == name_2)

print("name_1.lower() = name_2.lower() I predict True")
print(name_1.lower() == name_2.lower())

print("name_1 != name_2 I predict True ")
print(name_1 != name_2)

print("name_1.lower() != name_2.lower() I predict False")
print(name_1.lower() != name_2.lower())



print("Tests using the lower() function")
car_1 = "Audi"
car_2 = "audi"

print("car_1.lower() == car2.lower() I predict True")
print(car_1.lower() == car_2.lower())

print("car_1.lower() != car_2.lower() I predict False")
print(car_1.lower() != car_2.lower())


print(" Numerical tests involving equality and inequality, greater than and " \
"less than, greater than or equal to, and less than or equal to")

number_1 = 20
number_2 = 19
number_3 = 21

print("number_1 > 0 and number_1 < 30 I predict True")
print(number_1 > 0 and number_1 < 30)
print("number_1 > 0 and number_1 < 10 I predict False")
print(number_1 > 0 and number_1 < 10) 


print("number_2 <= number_1 I predict True")
print(number_2 <= number_1)
print("number_3 <= number_1 I predict False")
print(number_3 <= number_1)


print("number_2 >= number_1 I predict False")
print(number_2 >= number_1)
print("number_3 >= number_1 I predict True")
print(number_3 >= number_1)


print("Tests using the and keyword and the or keyword")
print("number_2 > 0 and number_1 < 100 I predict True")
print(number_2 > 0 and number_1 < 100) 
print("number_3 >= 22 and number_1 > 0 I predict False")
print(number_3 >= 22 and number_1 > 0)

print("number_2 > 0 or number_1 < 0 I predict True")
print(number_2 > 0 or  number_1 < 0) 
print("number_3 >= 22 or number_1 > 100 I predict False")
print(number_3 >= 22 or number_1 > 100)


print("Test whether an item is in a list")
tennis_players = ["Federer","Murray","Nadal","Novac"]
print('"Federer" in tennis_players I predict True')
print("Federer" in tennis_players) 
print('"Alcaraz" in tennis_players I predict False')
print("Alcaraz" in tennis_players)
print("Test whether an item is not in a list")
print('"Alcaraz" not in tennis_players I predict True')
print("Alcaraz" not in tennis_players)
print('"Federer" not in tennis_players I predict False')
print("Federer" not in tennis_players)
