#Normal list comprehensions
cube = [x**3 for x in range(10)]
print(cube)

#list comprehensions using map
cube = list(map(lambda x : x**3, range(10)))
print