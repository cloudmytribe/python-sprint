# LISTS

#my_elements = ["apples", "Oranges", 1, 1.20] 
#print(type(my_elements))
#            0       1           2
fruits = ["apple", "mango", "pineapple"]
#            -3         -2           -1
print(fruits)

#scores = [1, 10, 50, 100]
#print(scores)


print("My 2nd most favourite fruit is", fruits[1].upper())

# Modifying elements in a list

fruits[-2] = "blue berries"

print(fruits)

# Add elements into a list 

# to end of the list

fruits.append("avocado")
fruits.append("peach")
print(fruits)

# add elements to middle of the list

# ['apple', 'blue berries', 'pineapple', 'avocado', 'peach']

fruits.insert(2, "strawberries")
print(fruits)

# ['apple', 'blue berries', 'strawberries', 'pineapple', 'avocado', 'peach']

#del fruits[0]

print(fruits)

# ['blue berries', 'strawberries', 'pineapple', 'avocado', 'peach']

#fruits.pop()
print(fruits)

# ['blue berries', 'strawberries', 'pineapple', 'avocado']

#fruits.pop(1)

print(fruits)


# ['blue berries', 'pineapple', 'avocado']

#fruits.remove("pineapple")

print(fruits)



scores = [100, 1000, 99, 12, 1, 10, 50, 100]

print("Scores before sort", scores)

#scores.sort()
#print("Scores after sort", scores.sort())

#print("This are the reversed sorted scores", sorted(scores))

print("Scores after sorted", scores)

scores.reverse()
print("scores after reverse", scores)

print(len(scores))
print(len(fruits))

scores.insert(9, 10)
print(scores)

cars = []
print(cars[-1])
