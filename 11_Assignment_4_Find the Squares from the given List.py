
numbers=[int(x) for x in input("input list of numbers:").split()]
result = map(lambda x:x*x,numbers)
print(list(result))

