
def sum(numbers):
    n=0
    for x in numbers:
        n=n+x
    return n
numbers=[int(x) for x in input("input list of numbers:").split()]
total=sum(numbers)
print(total)
